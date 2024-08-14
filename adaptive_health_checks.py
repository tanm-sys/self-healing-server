class AdaptiveHealthChecks:
    def __init__(self, config):
        self.config = config
        self.cpu_threshold = config['cpu_threshold']
        self.memory_threshold = config['memory_threshold']
        self.disk_threshold = config['disk_threshold']
        self.response_time_threshold = config['response_time_threshold']

    def adjust_thresholds(self, health_data):
        # Example logic to adjust thresholds dynamically based on historical data
        self.cpu_threshold = min(100, self.cpu_threshold + (health_data['cpu_usage'] - self.cpu_threshold) * 0.1)
        self.memory_threshold = min(100, self.memory_threshold + (health_data['memory_usage'] - self.memory_threshold) * 0.1)
        self.disk_threshold = min(100, self.disk_threshold + (health_data['disk_usage'] - self.disk_threshold) * 0.1)
        self.response_time_threshold = min(10, self.response_time_threshold + (health_data['response_time'] - self.response_time_threshold) * 0.1)
