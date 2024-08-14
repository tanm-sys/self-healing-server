class DynamicThresholds:
    def __init__(self, initial_thresholds):
        self.thresholds = initial_thresholds

    def update_thresholds(self, health_data):
        for key, value in health_data.items():
            if key in self.thresholds:
                self.thresholds[key] = min(100, self.thresholds[key] + (value - self.thresholds[key]) * 0.1)
