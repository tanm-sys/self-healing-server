---

# Self-Healing Server

This project is a self-healing server system designed to monitor its own health and automatically take corrective actions when issues are detected. It includes features such as adaptive health checks, dynamic threshold adjustments, distributed monitoring, and leverages machine learning for anomaly detection.

## Features

- **Health Checks**: Periodically checks CPU usage, memory usage, disk space, and response time.
- **Adaptive Thresholds**: Dynamically adjusts health thresholds based on historical data.
- **Self-Healing Actions**: Automatically restarts services when thresholds are exceeded.
- **Distributed Monitoring**: Monitors multiple servers or services.
- **Error Handling**: Robust error handling and logging for unhandled exceptions.
- **Alerts**: Sends alerts for high resource usage and failed self-healing actions.
- **Prometheus Integration**: Provides metrics for monitoring with Prometheus.
- **Machine Learning Integration**: Uses ML models for anomaly detection and root cause analysis.
- **Customizable Health Checks**: Easily add new health checks as needed.
- **Scalable Architecture**: Designed to scale across multiple servers and services.
- **Historical Data Storage**: Stores health check data for trend analysis and future predictions.
- **Web Dashboard**: A user-friendly web dashboard for real-time monitoring and reporting.

## Project Structure

```
.
├── config.json                # Configuration file for monitoring settings
├── main.py                    # The main entry point to start the server
├── health_checks.py           # Functions for health checks
├── anomaly_detection.py       # Anomaly detection functions
├── alerts.py                  # Functions for sending alerts
├── service_manager.py         # Functions to manage services
├── logging_setup.py           # Logging setup and configuration
├── prometheus_metrics.py      # Prometheus metrics setup and handling
├── adaptive_health_checks.py  # Adaptive health check implementations
├── error_handling.py          # Error handling utilities
├── dynamic_thresholds.py      # Dynamic threshold adjustment logic
├── distributed_monitoring.py  # Distributed monitoring functionalities
├── historical_data.py         # Functions to store and manage historical data
├── web_dashboard              # Directory containing web dashboard files
│   ├── app.py                 # Flask app for the web dashboard
│   └── templates              # HTML templates for the web dashboard
└── requirements.txt           # List of project dependencies
```

## Configuration

Create a `config.json` file in the root directory with the following structure:

```json
{
  "server_urls": [
    "http://localhost:8000/health"
  ],
  "cpu_threshold": 80,
  "memory_threshold": 80,
  "disk_threshold": 90,
  "response_time_threshold": 2.0,
  "check_interval": 60,
  "alert_email": "admin@example.com",
  "ml_model_path": "models/anomaly_detector.pkl",
  "historical_data_db": "data/health_data.db",
  "dashboard_port": 5000
}
```

- **`server_urls`**: List of URLs for distributed monitoring.
- **`cpu_threshold`**: CPU usage threshold for self-healing.
- **`memory_threshold`**: Memory usage threshold for self-healing.
- **`disk_threshold`**: Disk usage threshold for self-healing.
- **`response_time_threshold`**: Response time threshold for self-healing.
- **`check_interval`**: Interval (in seconds) between health checks.
- **`alert_email`**: Email address to send alerts.
- **`ml_model_path`**: Path to the machine learning model for anomaly detection.
- **`historical_data_db`**: Path to the SQLite database for storing historical data.
- **`dashboard_port`**: Port on which the web dashboard will run.

## Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/yourusername/self-healing-server.git
   cd self-healing-server
   ```

2. **Create and Activate a Virtual Environment** (Optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Server

1. **Set Up Configuration**: Ensure `config.json` is properly set up in the root directory.

2. **Start the Server**:

   ```sh
   python main.py
   ```

   The server will start and begin monitoring based on the configuration. Health checks will be performed, and corrective actions will be taken if necessary.

3. **Start the Web Dashboard** (Optional):

   ```sh
   python web_dashboard/app.py
   ```

   Access the dashboard at `http://localhost:5000` (default port).

## Development

### Adding New Health Checks

To add new health checks:

1. Implement the check in `health_checks.py`.
2. Update `adaptive_health_checks.py` to include your new check.
3. Ensure that metrics are updated, and alerts are sent if needed.

### Adding New Alerts

To add new alert types:

1. Update `alerts.py` with new alert functions.
2. Modify `adaptive_health_checks.py` to call these functions when appropriate.

### Updating Logging

Modify `logging_setup.py` to configure logging levels, formats, and destinations as needed.

### Machine Learning Integration

To integrate new ML models:

1. Train your model and save it in a compatible format (e.g., pickle).
2. Update `anomaly_detection.py` to load and use the new model.
3. Adjust `config.json` to point to the new model path.

### Historical Data Storage

1. Implement data storage functions in `historical_data.py`.
2. Ensure health checks and anomalies are logged into the database.
3. Use stored data for trend analysis and threshold adjustments.

## Testing

Ensure that all components are properly tested. Unit tests can be added for individual functions and integration tests for the system as a whole.

### Running Tests

1. **Run Unit Tests**:

   ```sh
   python -m unittest discover tests
   ```

2. **Run Integration Tests**:

   ```sh
   python -m unittest discover integration_tests
   ```

## Troubleshooting

- **Service Not Restarting**: Ensure that the `restart_service` function in `service_manager.py` is correctly implemented and has the necessary permissions.
- **High CPU Usage Alerts**: Adjust the CPU threshold in `config.json` or review the CPU check logic in `adaptive_health_checks.py`.
- **Distributed Monitoring Issues**: Verify that server URLs in `config.json` are correct and that the monitored services are up and running.
- **ML Model Not Loading**: Ensure the model path in `config.json` is correct and the model is compatible.

## Deployment

### Docker

To deploy the server using Docker:

1. **Build the Docker Image**:

   ```sh
   docker build -t self-healing-server .
   ```

2. **Run the Docker Container**:

   ```sh
   docker run -d -p 8000:8000 -p 5000:5000 --name self-healing-server self-healing-server
   ```

### Kubernetes

To deploy the server using Kubernetes:

1. **Create a Deployment YAML**:

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: self-healing-server
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: self-healing-server
     template:
       metadata:
         labels:
           app: self-healing-server
       spec:
         containers:
         - name: self-healing-server
           image: yourusername/self-healing-server:latest
           ports:
           - containerPort: 8000
           - containerPort: 5000
           volumeMounts:
           - name: config-volume
             mountPath: /app/config.json
             subPath: config.json
         volumes:
         - name: config-volume
           configMap:
             name: self-healing-server-config
   ```

2. **Apply the Deployment**:

   ```sh
   kubectl apply -f deployment.yaml
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
