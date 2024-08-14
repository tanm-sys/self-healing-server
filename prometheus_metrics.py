from prometheus_client import start_http_server, Gauge

class PrometheusMetrics:
    def __init__(self):
        self.cpu_usage_gauge = Gauge('cpu_usage', 'CPU Usage')
        self.memory_usage_gauge = Gauge('memory_usage', 'Memory Usage')
        self.disk_usage_gauge = Gauge('disk_usage', 'Disk Usage')
        self.response_time_gauge = Gauge('response_time', 'Response Time')
        start_http_server(8000)

    def update_metrics(self, health_data):
        self.cpu_usage_gauge.set(health_data['cpu_usage'])
        self.memory_usage_gauge.set(health_data['memory_usage'])
        self.disk_usage_gauge.set(health_data['disk_usage'])
        self.response_time_gauge.set(health_data['response_time'])
