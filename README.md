---
# Self-Healing Server

Welcome to the Self-Healing Server project! This repository contains a powerful, adaptable server system designed to monitor its health and automatically take corrective actions when issues are detected. The system includes advanced features such as adaptive health checks, dynamic threshold adjustments, distributed monitoring, and leverages machine learning for anomaly detection.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Server](#running-the-server)
- [Running the Web Dashboard](#running-the-web-dashboard)
- [Unit Tests](#unit-tests)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Health Checks**: Periodically checks CPU usage, memory usage, disk space, and response time.
- **Adaptive Thresholds**: Dynamically adjusts health thresholds based on historical data.
- **Self-Healing Actions**: Automatically restarts services when thresholds are exceeded.
- **Distributed Monitoring**: Monitors multiple servers or services.
- **Error Handling**: Robust error handling and logging for unhandled exceptions.
- **Alerts**: Sends alerts for high resource usage and failed self-healing actions.
- **Prometheus Integration**: Provides metrics for monitoring with Prometheus.
- **Machine Learning**: Utilizes anomaly detection for more accurate health assessments.

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
└── web_dashboard
    ├── app.py                # Flask app for web dashboard
    ├── static                # Static files (CSS, JS, images)
    └── templates             # HTML templates for Flask
        └── index.html        # Main dashboard page
```

## Installation

### Prerequisites

- Python 3.x
- Virtual Environment (optional but recommended)

### Steps

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/self-healing-server.git
   cd self-healing-server
   ```

2. **Create and Activate Virtual Environment**:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

Create a `config.json` file in the root directory with the following structure:

```json
{
  "server_urls": ["http://localhost:8000/health"],
  "cpu_threshold": 80,
  "memory_threshold": 80,
  "disk_threshold": 90,
  "response_time_threshold": 2.0,
  "check_interval": 60,
  "alert_email": "admin@example.com",
  "log_level": "INFO"
}
```

- `server_urls`: List of URLs for distributed monitoring.
- `cpu_threshold`: CPU usage threshold for self-healing.
- `memory_threshold`: Memory usage threshold for self-healing.
- `disk_threshold`: Disk usage threshold for self-healing.
- `response_time_threshold`: Response time threshold for self-healing.
- `check_interval`: Interval (in seconds) between health checks.
- `alert_email`: Email address to send alerts to.
- `log_level`: Logging level (e.g., INFO, DEBUG).

## Running the Server

1. **Set Up Configuration**: Ensure `config.json` is properly set up in the root directory.
2. **Start the Server**:
   ```sh
   python main.py
   ```

The server will start and begin monitoring based on the configuration. Health checks will be performed, and corrective actions will be taken if necessary.

## Running the Web Dashboard

1. **Navigate to Web Dashboard Directory**:
   ```sh
   cd web_dashboard
   ```

2. **Activate Virtual Environment**:
   ```sh
   venv\Scripts\activate
   ```

3. **Run the Flask App**:
   ```sh
   python app.py
   ```

4. **Access the Dashboard**: Open a web browser and navigate to `http://localhost:5000`.

## Unit Tests

Run the unit tests to ensure everything is working as expected:

```sh
python -m unittest discover tests
```

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

## Contributing

We welcome contributions to this project! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to get started.

### Contribution Workflow

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Future Improvements

- **Enhanced Anomaly Detection**: Improve the machine learning models for better anomaly detection accuracy.
- **User Interface**: Create a more user-friendly and visually appealing web dashboard.
- **Integration with Other Monitoring Tools**: Add support for integrating with other popular monitoring tools and services.
- **Scalability**: Enhance the system to support larger and more complex infrastructures.

## Troubleshooting

- **Service Not Restarting**: Ensure that the `restart_service` function in `service_manager.py` is correctly implemented and has the necessary permissions.
- **High CPU Usage Alerts**: Adjust the CPU threshold in `config.json` or review the CPU check logic in `adaptive_health_checks.py`.
- **Distributed Monitoring Issues**: Verify that server URLs in `config.json` are correct and that the monitored services are up and running.

By following these steps, you should be able to set up and run the self-healing server on your localhost, monitor its health, and view the data through the web dashboard. Your contributions and feedback are highly appreciated!
---
