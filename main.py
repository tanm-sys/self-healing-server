import asyncio
from adaptive_health_checks import adaptive_cpu_check, adaptive_memory_check, adaptive_disk_check, adaptive_response_time_check
from anomaly_detection import detect_anomalies
from prometheus_metrics import start_prometheus_server
from logging_setup import setup_logging
from error_handling import handle_exception
from distributed_monitoring import monitor_servers, load_config

def main():
    setup_logging()
    start_prometheus_server()

    config = load_config()
    server_urls = config["server_urls"]

    async def periodic_health_checks():
        while True:
            await asyncio.gather(
                adaptive_cpu_check(),
                adaptive_memory_check(),
                adaptive_disk_check(),
                adaptive_response_time_check(),
                monitor_servers(server_urls)
            )
            detect_anomalies()
            await asyncio.sleep(config["check_interval"])

    asyncio.run(periodic_health_checks())

if __name__ == "__main__":
    main()
  
