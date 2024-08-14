import asyncio
import json
from health_checks import perform_health_checks
from adaptive_health_checks import AdaptiveHealthChecks
from anomaly_detection import AnomalyDetection
from service_manager import ServiceManager
from alerts import AlertManager
from logging_setup import setup_logging
from distributed_monitoring import DistributedMonitoring
from prometheus_metrics import PrometheusMetrics
from historical_data import HistoricalData

async def main():
    with open('config.json') as config_file:
        config = json.load(config_file)

    setup_logging()
    adaptive_health_checks = AdaptiveHealthChecks(config)
    anomaly_detection = AnomalyDetection(config['ml_model_path'])
    service_manager = ServiceManager()
    alert_manager = AlertManager(config['alert_email'])
    prometheus_metrics = PrometheusMetrics()
    distributed_monitoring = DistributedMonitoring(config['server_urls'])
    historical_data = HistoricalData(config['historical_data_db'])

    while True:
        health_data = await perform_health_checks(config)
        adaptive_health_checks.adjust_thresholds(health_data)
        anomalies = anomaly_detection.detect_anomalies(health_data)
        
        historical_data.store_data(health_data)  # Store the health data

        if anomalies:
            alert_manager.send_alert(str(anomalies))
            service_manager.restart_services(anomalies)

        prometheus_metrics.update_metrics(health_data)
        distributed_monitoring.collect_data()
        
        await asyncio.sleep(config['check_interval'])

if __name__ == "__main__":
    asyncio.run(main())
