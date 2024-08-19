import os
import time
import json
import logging
import psutil
import requests
import smtplib
from email.mime.text import MIMEText
from prometheus_client import start_http_server, Gauge
from threading import Thread
from typing import List, Dict, Any

# Configuration and log file paths
CONFIG_FILE_PATH = os.getenv('CONFIG_FILE_PATH', 'config.json')
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'server_monitor.log')

def load_config() -> Dict[str, Any]:
    """Load configuration from the JSON file."""
    try:
        with open(CONFIG_FILE_PATH) as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {CONFIG_FILE_PATH}")
        raise
    except PermissionError:
        logging.error(f"Permission denied: {CONFIG_FILE_PATH}")
        raise
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the configuration file.")
        raise
    except Exception as e:
        logging.error(f"Unexpected error while loading configuration: {e}")
        raise

def setup_logging(level: str) -> None:
    """Setup logging configuration."""
    log_level = getattr(logging, level.upper(), logging.INFO)
    
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    
    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def perform_health_checks() -> Dict[str, Any]:
    """Perform health checks on CPU, memory, disk, and server response."""
    results = {
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'response_time': check_server_response(),
        'needs_restart': False  # Initialize needs_restart key
    }
    
    # Example condition for setting needs_restart
    config = load_config()
    if results['cpu_usage'] > config['cpu_threshold']:
        results['needs_restart'] = True
    
    logging.debug(f"Health check results: {results}")
    return results

def check_server_response() -> float:
    """Check server response time."""
    try:
        response = requests.get('http://localhost:7777/health', timeout=20)
        response_time = response.elapsed.total_seconds()
        if response.status_code == 200:
            logging.debug(f"Server response time: {response_time} seconds")
            return response_time
        else:
            logging.error(f"Health check failed with status code: {response.status_code}")
            return float('inf')
    except requests.RequestException as e:
        logging.error(f"Health check failed: {e}")
        return float('inf')

def verify_server_is_running() -> None:
    """Verify that the server is running and accessible."""
    try:
        response = requests.get('http://localhost:7777/health', timeout=20)
        if response.status_code == 200:
            logging.info("Server is running and accessible.")
        else:
            logging.error(f"Server is running but returned status code {response.status_code}.")
    except requests.RequestException as e:
        logging.error(f"Failed to connect to the server: {e}")

def detect_anomalies(current_value: float, historical_data: List[float], threshold: float) -> bool:
    """Detect anomalies based on historical data."""
    if len(historical_data) < 5:  # Ensure there is enough data
        return False
    
    avg = sum(historical_data) / len(historical_data)
    deviation = abs(current_value - avg)
    is_anomaly = deviation > threshold
    logging.debug(f"Anomaly detection - Current Value: {current_value}, Avg: {avg}, Deviation: {deviation}, Is Anomaly: {is_anomaly}")
    return is_anomaly

def send_alert(message: str) -> None:
    """Send an alert email."""
    sender_email = "rohanbelsare113@gmail.com"
    receiver_email = "laukikbelsare113@gmail.com"
    
    msg = MIMEText(message)
    msg['Subject'] = 'Server Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)
            logging.info('Alert sent successfully.')
    except Exception as e:
        logging.error(f"Failed to send alert: {e}")

def restart_service(service_name: str) -> None:
    """Restart the server service."""
    try:
        os.system(f'systemctl restart {service_name}')
        logging.info(f'Service {service_name} restarted successfully.')
    except Exception as e:
        logging.error(f"Failed to restart service {service_name}: {e}")

def start_prometheus_server(port: int) -> None:
    """Start the Prometheus metrics server."""
    def prometheus_thread():
        cpu_usage_gauge = Gauge('cpu_usage', 'CPU Usage in percent')
        memory_usage_gauge = Gauge('memory_usage', 'Memory Usage in percent')
        disk_usage_gauge = Gauge('disk_usage', 'Disk Usage in percent')
    
        start_http_server(port)
        logging.info(f"Prometheus metrics server started on port {port}")
        while True:
            cpu_usage_gauge.set(psutil.cpu_percent())
            memory_usage_gauge.set(psutil.virtual_memory().percent)
            disk_usage_gauge.set(psutil.disk_usage('/').percent)
            time.sleep(10)
    
    thread = Thread(target=prometheus_thread)
    thread.daemon = True
    thread.start()

def check_and_adapt_thresholds(results: Dict[str, Any], historical_data: Dict[str, List[float]]) -> None:
    """Check health results and adapt thresholds if necessary."""
    thresholds = load_config()
    
    cpu_anomaly = detect_anomalies(results['cpu_usage'], historical_data['cpu_usage'], thresholds['cpu_threshold'])
    memory_anomaly = detect_anomalies(results['memory_usage'], historical_data['memory_usage'], thresholds['memory_threshold'])
    disk_anomaly = detect_anomalies(results['disk_usage'], historical_data['disk_usage'], thresholds['disk_threshold'])
    response_anomaly = detect_anomalies(results['response_time'], historical_data['response_time'], thresholds['response_time_threshold'])
    
    if cpu_anomaly or memory_anomaly or disk_anomaly or response_anomaly:
        new_thresholds = {
            'cpu_threshold': thresholds['cpu_threshold'] + 5,
            'memory_threshold': thresholds['memory_threshold'] + 5,
            'disk_threshold': thresholds['disk_threshold'] + 5,
            'response_time_threshold': thresholds['response_time_threshold'] + 1
        }
        adjust_thresholds(new_thresholds)
        logging.info('Thresholds adjusted due to detected anomalies.')

def adjust_thresholds(new_thresholds: Dict[str, int]) -> None:
    """Adjust health check thresholds in the configuration."""
    try:
        with open(CONFIG_FILE_PATH, 'r+') as config_file:
            config = json.load(config_file)
            config.update(new_thresholds)
            config_file.seek(0)
            json.dump(config, config_file, indent=4)
            config_file.truncate()  # Remove any leftover content
    except PermissionError:
        logging.error(f"Permission denied: {CONFIG_FILE_PATH}")
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from the configuration file.")
    except Exception as e:
        logging.error(f"Unexpected error while adjusting thresholds: {e}")

def monitor_distributed_servers(server_urls: List[str]) -> None:
    """Monitor multiple distributed servers."""
    for url in server_urls:
        try:
            response = requests.get(url)
            if response.status_code != 200:
                logging.error(f"Server {url} is down.")
            else:
                logging.debug(f"Server {url} is up.")
        except requests.RequestException as e:
            logging.error(f"Error monitoring server {url}: {e}")

def main() -> None:
    """Main function to start the server and perform health checks."""
    config = load_config()
    setup_logging(config['log_level'])
    start_prometheus_server(config['prometheus_port'])
    
    historical_data = {
        'cpu_usage': [],
        'memory_usage': [],
        'disk_usage': [],
        'response_time': []
    }
    
    while True:
        try:
            verify_server_is_running()  # Check if the server is up and running
            results = perform_health_checks()
            
            # Add new results to historical data
            for key in historical_data:
                historical_data[key].append(results[key])
                # Limit the size of historical data to avoid memory leaks
                if len(historical_data[key]) > 100:
                    historical_data[key].pop(0)
            
            check_and_adapt_thresholds(results, historical_data)
            
            if results['needs_restart']:
                restart_service(config['service_name'])
                send_alert(f"{config['service_name']} has been restarted due to health check failure.")
            
            monitor_distributed_servers(config['server_urls'])
            
            time.sleep(config['check_interval'])
        except KeyboardInterrupt:
            logging.info("Server monitoring stopped by user.")
            break
        except Exception as e:
            logging.error(f"Unexpected error in main loop: {e}")

if __name__ == "__main__":
    main()


