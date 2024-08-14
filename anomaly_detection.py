import pickle
import numpy as np

class AnomalyDetection:
    def __init__(self, model_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)

    def detect_anomalies(self, health_data):
        data = np.array([health_data['cpu_usage'], health_data['memory_usage'], health_data['disk_usage'], health_data['response_time']]).reshape(1, -1)
        anomalies = self.model.predict(data)
        return anomalies
