import psutil
import logging
from prometheus_metrics import cpu_gauge, memory_gauge, disk_gauge, response_time_gauge
from alerts import send_alert
from service_manager import restart_service
from dynamic_thresholds import DynamicThresholds
import json

# Load config
def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

config = load_config()
dynamic_thresholds = DynamicThresholds()

async def adaptive_cpu_check():
    cpu_usage = psutil.cpu_percent(interval=1)
    dynamic_thresholds.add_cpu_usage(cpu_usage)
    dynamic_thresholds.update_thresholds()
    cpu_gauge.set(cpu_usage)
    if cpu_usage > dynamic_thresholds.cpu_threshold:
        logging.warning("High CPU usage detected: %.2f%%", cpu_usage)
        send_alert("High CPU Usage", f"CPU usage is {cpu_usage:.2f}%")
        adaptive_recovery('cpu_intensive_service', 'CPU')

async def adaptive_memory_check():
    memory = psutil.virtual_memory()
    dynamic_thresholds.add_memory_usage(memory.percent)
    dynamic_thresholds.update_thresholds()
    memory_gauge.set(memory.percent)
    if memory.percent > dynamic_thresholds.memory_threshold:
        logging.warning("High memory usage detected: %.2f%%", memory.percent)
        send_alert("High Memory Usage", f"Memory usage is {memory.percent:.2f}%")
        adaptive_recovery('memory_intensive_service', 'Memory')

async def adaptive_disk_check():
    disk = psutil.disk_usage('/')
    dynamic_thresholds.add_disk_usage(disk.percent)
    dynamic_thresholds.update_thresholds()
    disk_gauge.set(disk.percent)
    if disk.percent > dynamic_thresholds.disk_threshold:
        logging.warning("High disk usage detected: %.2f%%", disk.percent)
        send_alert("High Disk Usage", f"Disk usage is {disk.percent:.2f}%")
        adaptive_recovery('disk_intensive_service', 'Disk')

async def adaptive_response_time_check():
    import time, os
    start_time = time.time()
    response = os.system("ping -c 1 localhost > /dev/null 2>&1")
    end_time = time.time()
    response_time = end_time - start_time
    dynamic_thresholds.add_response_time(response_time)
    dynamic_thresholds.update_thresholds()
    response_time_gauge.set(response_time)
    if response != 0 or response_time > dynamic_thresholds.response_time_threshold:
        logging.warning("High response time detected: %.2f seconds", response_time)
        send_alert("High Response Time", f"Response time is {response_time:.2f} seconds")
        adaptive_recovery('network_service', 'Response Time')

def adaptive_recovery(service_name, metric):
    """ Adaptive recovery mechanism that dynamically restarts services based on metric type """
    try:
        logging.info(f"Attempting to recover {service_name} due to high {metric}")
        restart_service(service_name)
    except Exception as e:
        logging.error(f"Failed to recover {service_name} due to {e}")
        send_alert(f"Service Recovery Failed: {service_name}", f"Failed to recover {service_name} due to {e}")
      
