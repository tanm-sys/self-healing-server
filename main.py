import time
import json
import logging
import psutil
import requests
import smtplib
import os
from email.mime.text import MIMEText
from prometheus_client import start_http_server, Gauge
from sklearn.ensemble import IsolationForest
import numpy as np
from typing import List, Dict, Any

# Configuration file path
CONFIG_FILE_PATH = 'config.json'

def load_config() -> Dict[str, Any]:
    """Load configuration from the JSON file."""
    with open(CONFIG_FILE_PATH) as config_file:
        return json.load(config_file)

def setup_logging(level: str) -> None:
    """Setup logging configuration."""
    logging.basicConfig(level=getattr(logging, level.upper()), format='%(asctime)s - %(levelname)s - %(message)s')

def perform_health_checks() -> Dict[str, Any]:
    """Perform health checks on CPU, memory, disk, and server response."""
    results = {
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'response_time': check_server_response(),
        'needs_restart': False
    }
    return results

def check_server_response() -> float:
    """Check server response time."""
    try:
        response = requests.get('http://localhost:8000/health', timeout=5)
        return response.elapsed.total_seconds()
    except requests.RequestException as e:
        logging.error(f"Health check failed: {e}")
        return float('inf')

def detect_anomalies(data: List[float]) -> np.ndarray:
    """Detect anomalies in the given data using Isolation Forest."""
    model = IsolationForest(contamination=0.1)
    data = np.array(data).reshape(-1, 1)
    model.fit(data)
    return model.predict(data)

def send_alert(email_address: str) -> None:
    """Send an alert email."""
    msg = MIMEText('server failed')
    msg['Subject'] = 'Server Alert'
    msg['From'] = 'rohanbelsare113@gmail.com'  # Replace with your Gmail address
    msg['To'] = 'laukikbelsare@gmail.com'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login('your_email@gmail.com', 'vvaz bjng qoaz trto')  # Replace with your Gmail and App Password
            server.send_message(msg)
            logging.info('Alert sent successfully.')
    except Exception as e:
        logging.error(f"Failed to send alert: {e}")

def restart_service() -> None:
    """Restart the server service."""
    try:
        os.system('systemctl restart my_service')
        logging.info('Service restarted successfully.')
    except Exception as e:
        logging.error(f"Failed to restart service: {e}")

def start_prometheus_server(port: int) -> None:
    """Start the Prometheus metrics server."""
    cpu_usage_gauge = Gauge('cpu_usage', 'CPU Usage in percent')
    memory_usage_gauge = Gauge('memory_usage', 'Memory Usage in percent')
    disk_usage_gauge = Gauge('disk_usage', 'Disk Usage in percent')

    start_http_server(port)
    while True:
        cpu_usage_gauge.set(psutil.cpu_percent())
        memory_usage_gauge.set(psutil.virtual_memory().percent)
        disk_usage_gauge.set(psutil.disk_usage('/').percent)
        time.sleep(10)

def check_and_adapt_thresholds(results: Dict[str, Any]) -> None:
    """Check health results and adapt thresholds if necessary."""
    thresholds = load_config()
    anomalies = detect_anomalies([results['cpu_usage'], results['memory_usage'], results['disk_usage'], results['response_time']])
    
    if anomalies[0] == -1:
        new_thresholds = {
            'cpu_threshold': thresholds['cpu_threshold'] + 5,
            'memory_threshold': thresholds['memory_threshold'] + 5
        }
        adjust_thresholds(new_thresholds)

def adjust_thresholds(new_thresholds: Dict[str, int]) -> None:
    """Adjust health check thresholds in the configuration."""
    with open(CONFIG_FILE_PATH, 'r+') as config_file:
        config = json.load(config_file)
        config.update(new_thresholds)
        config_file.seek(0)
        json.dump(config, config_file, indent=4)

def monitor_distributed_servers(server_urls: List[str]) -> None:
    """Monitor multiple distributed servers."""
    for url in server_urls:
        try:
            response = requests.get(url)
            if response.status_code != 200:
                logging.error(f"Server {url} is down.")
        except requests.RequestException as e:
            logging.error(f"Error monitoring server {url}: {e}")

def main() -> None:
    """Main function to start the server and perform health checks."""
    config = load_config()
    setup_logging(config['log_level'])
    start_prometheus_server(config['prometheus_port'])
    
    while True:
        try:
            results = perform_health_checks()
            check_and_adapt_thresholds(results)
            
            if results['needs_restart']:
                restart_service()
                send_alert(config['alert_email'], 'Service restarted due to health check failure.')
            
            monitor_distributed_servers(config['server_urls'])
            time.sleep(config['check_interval'])
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()

