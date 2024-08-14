from prometheus_client import start_http_server, Gauge

cpu_usage_gauge = Gauge('cpu_usage', 'CPU usage percentage')
memory_usage_gauge = Gauge('memory_usage', 'Memory usage percentage')
disk_usage_gauge = Gauge('disk_usage', 'Disk usage percentage')
response_time_gauge = Gauge('response_time', 'Response time in seconds')

def setup_prometheus_metrics():
    start_http_server(8001)
