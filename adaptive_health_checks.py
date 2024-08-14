import structlog

logger = structlog.get_logger()

def perform_adaptive_health_checks(health_status, anomalies, config, service_manager, alert_manager):
    for idx in anomalies:
        cpu, memory, disk, response_time = health_status[idx]

        if cpu > config['cpu_threshold']:
            service_manager.restart_service('cpu_intensive_service')
            alert_manager.send_alert('CPU usage exceeded threshold. Restarted service.')

        if memory > config['memory_threshold']:
            service_manager.restart_service('memory_intensive_service')
            alert_manager.send_alert('Memory usage exceeded threshold. Restarted service.')

        if disk > config['disk_threshold']:
            service_manager.restart_service('disk_intensive_service')
            alert_manager.send_alert('Disk usage exceeded threshold. Restarted service.')

        if response_time > config['response_time_threshold']:
            service_manager.restart_service('web_service')
            alert_manager.send_alert('Response time exceeded threshold. Restarted service.')
