import os

class ServiceManager:
    def restart_services(self, anomalies):
        for anomaly in anomalies:
            if anomaly == 'cpu_usage':
                os.system('systemctl restart some_service')
            elif anomaly == 'memory_usage':
                os.system('systemctl restart some_service')
            elif anomaly == 'disk_usage':
                os.system('systemctl restart some_service')
            elif anomaly == 'response_time':
                os.system('systemctl restart some_service')
