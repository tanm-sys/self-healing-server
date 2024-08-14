import asyncio
import logging
import structlog

from health_checks import check_health
from anomaly_detection import detect_anomalies
from alerts import AlertManager
from service_manager import ServiceManager
from prometheus_metrics import setup_prometheus_metrics
from adaptive_health_checks import perform_adaptive_health_checks
from distributed_monitoring import monitor_servers
from logging_setup import setup_logging
from config import load_config

# Load configuration
config = load_config('config.json')

# Setup logging
setup_logging(config['log_level'])
logger = structlog.get_logger()

# Initialize services
alert_manager = AlertManager(config['alert_email'])
service_manager = ServiceManager()

async def main():
    setup_prometheus_metrics()
    
    while True:
        try:
            health_status = await check_health(config['server_urls'])
            anomalies = detect_anomalies(health_status)
            
            perform_adaptive_health_checks(health_status, anomalies, config, service_manager, alert_manager)
            monitor_servers(config['server_urls'])
            
            await asyncio.sleep(config['check_interval'])
        except Exception as e:
            logger.error("Error in main loop", error=str(e))

if __name__ == "__main__":
    asyncio.run(main())
