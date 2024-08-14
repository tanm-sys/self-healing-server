import numpy as np

class DynamicThresholds:
    def __init__(self):
        self.cpu_history = []
        self.memory_history = []
        self.disk_history = []
        self.response_time_history = []

    def update_thresholds(self):
        self.cpu_threshold = np.percentile(self.cpu_history, 95)
        self.memory_threshold = np.percentile(self.memory_history, 95)
        self.disk_threshold = np.percentile(self.disk_history, 95)
        self.response_time_threshold = np.percentile(self.response_time_history, 95)

    def add_cpu_usage(self, usage):
        self.cpu_history.append(usage)
        if len(self.cpu_history) > 100:
            self.cpu_history.pop(0)

    def add_memory_usage(self, usage):
        self.memory_history.append(usage)
        if len(self.memory_history) > 100:
            self.memory_history.pop(0)

    def add_disk_usage(self, usage):
        self.disk_history.append(usage)
        if len(self.disk_history) > 100:
            self.disk_history.pop(0)

    def add_response_time(self, time):
        self.response_time_history.append(time)
        if len(self.response_time_history) > 100:
            self.response_time_history.pop(0)
          
