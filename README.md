---

![Self-Healing Server](https://img.shields.io/badge/status-active-green) ![Python Version](https://img.shields.io/badge/python-3.7%2B-blue) ![License](https://img.shields.io/badge/license-MIT-blue) ![Build Status](https://img.shields.io/github/workflow/status/yourusername/self-healing-server/CI) ![Code Quality](https://img.shields.io/codecov/c/github/yourusername/self-healing-server)

Welcome to the **Self-Healing Server** project! This advanced server management system is designed to autonomously monitor, diagnose, and manage server health to ensure uninterrupted performance and high availability. Leveraging state-of-the-art technologies such as adaptive health checks, dynamic threshold adjustments, and machine learning-based anomaly detection, our system delivers comprehensive and proactive server management.

## 📚 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Server](#running-the-server)
- [Running the Web Dashboard](#running-the-web-dashboard)
- [Unit Tests](#unit-tests)
- [Development](#development)
- [Contributing](#contributing)
- [Future Improvements](#future-improvements)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## 🚀 Features

- **🔍 Health Checks**: 
  - Monitors vital server metrics including CPU usage, memory consumption, disk space, and response time.
  - Provides a detailed view of server health and performance.
  
- **⚙️ Adaptive Thresholds**:
  - Dynamically adjusts health check thresholds based on historical data and trends.
  - Adapts to changes in server workload and usage patterns to reduce false positives.

- **🔄 Self-Healing Actions**:
  - Automatically performs corrective actions, such as restarting services or reallocating resources, when thresholds are exceeded.
  - Ensures minimal downtime and consistent performance.

- **🌐 Distributed Monitoring**:
  - Enables monitoring of multiple servers or services from a central location.
  - Aggregates data for a comprehensive view of the entire infrastructure.

- **🛠️ Error Handling**:
  - Implements robust error handling mechanisms to capture, log, and diagnose issues effectively.
  - Provides detailed error reports and stack traces for troubleshooting.

- **📧 Alerts**:
  - Configurable alerting system for notifying administrators of critical issues, such as high resource usage or failed self-healing actions.
  - Supports email notifications and integration with other messaging services.

- **📊 Prometheus Integration**:
  - Exposes metrics in a format compatible with Prometheus for advanced monitoring and alerting.
  - Facilitates the creation of custom dashboards and alerts in Prometheus.

- **🤖 Machine Learning**:
  - Utilizes machine learning models to detect anomalies and predict potential issues before they impact server performance.
  - Continuously improves anomaly detection accuracy based on historical data.

## 🏗️ Project Structure

The project is organized into the following modules:

```
.
├── config.json                # Configuration file for monitoring settings
├── main.py                    # Main entry point to start the server
├── health_checks.py           # Functions to perform various health checks
├── anomaly_detection.py       # Machine learning models and functions for anomaly detection
├── alerts.py                  # Functions to manage and send alerts
├── service_manager.py         # Manages service restarts and recovery actions
├── logging_setup.py           # Configuration for logging and error reporting
├── prometheus_metrics.py      # Setup and management of Prometheus metrics
├── adaptive_health_checks.py  # Implements adaptive health check adjustments
├── error_handling.py          # Utilities for comprehensive error handling
├── dynamic_thresholds.py      # Logic for dynamically adjusting thresholds
├── distributed_monitoring.py  # Functions for monitoring multiple servers
└── web_dashboard
    ├── app.py                # Flask application for the web dashboard
    ├── static                # Static files (CSS, JS, images) for the dashboard
    └── templates             # HTML templates for the dashboard
        └── index.html        # Main page of the web dashboard
```

## 🛠️ Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure that you have Python 3.7 or later installed.
- **Virtual Environment** (recommended): To create an isolated environment for the project.

### Steps

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/tanm-sys/self-healing-server.git
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

4. **Install Additional Development Tools** (optional but recommended):
   ```sh
   pip install pytest pylint
   ```

## ⚙️ Configuration

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
  "log_level": "INFO",
  "prometheus_port": 9090
}
```

- **`server_urls`**: List of URLs for distributed health checks.
- **`cpu_threshold`**: CPU usage percentage that triggers self-healing actions.
- **`memory_threshold`**: Memory usage percentage threshold for self-healing.
- **`disk_threshold`**: Disk usage percentage threshold for self-healing.
- **`response_time_threshold`**: Maximum acceptable response time in seconds.
- **`check_interval`**: Interval (in seconds) between health checks.
- **`alert_email`**: Email address for receiving alerts.
- **`log_level`**: Logging level (e.g., INFO, DEBUG).
- **`prometheus_port`**: Port for Prometheus metrics endpoint.

## 🏃 Running the Server

1. **Set Up Configuration**: Ensure that `config.json` is correctly configured according to your environment.
2. **Start the Server**:
   ```sh
   python main.py
   ```

The server will initialize and start performing health checks based on the configuration. It will automatically take corrective actions if necessary.

## 🌐 Running the Web Dashboard

1. **Navigate to the Web Dashboard Directory**:
   ```sh
   cd web_dashboard
   ```

2. **Activate Virtual Environment**:
   ```sh
   venv\Scripts\activate
   ```

3. **Run the Flask Application**:
   ```sh
   python app.py
   ```

4. **Access the Dashboard**: Open a web browser and visit `http://localhost:5000` to interact with the dashboard.

## 🧪 Unit Tests

Unit tests are essential for validating the functionality of the system. To run tests:

1. **Run Unit Tests**:
   ```sh
   python -m unittest discover tests
   ```

2. **For Advanced Testing**:
   ```sh
   pip install pytest
   pytest
   ```

Ensure that all new features and bug fixes are accompanied by appropriate tests.

## 🛠️ Development

### Adding New Health Checks

1. **Implement the Check**: Add the new health check function in `health_checks.py`.
2. **Integrate with Adaptive Health Checks**: Update `adaptive_health_checks.py` to incorporate the new check.
3. **Add Tests**: Write unit tests for the new health check in the `tests` directory.

### Adding New Alerts

1. **Update Alerts Module**: Add new alerting functionality to `alerts.py`.
2. **Modify Health Checks**: Adjust `adaptive_health_checks.py` to trigger new alerts as necessary.
3. **Test Alerts**: Ensure the new alerts are tested and functioning correctly.

### Updating Logging

Enhance logging capabilities by updating `logging_setup.py`:
- **Configure Logging Levels**: Define levels such as INFO, DEBUG, ERROR.
- **Set Logging Formats**: Specify formats for logs, such as JSON or plain text.
- **Log Destinations**: Set up log destinations, including files and remote logging services.

### Enhancing Anomaly Detection

- **Refine ML Models**: Improve models in `anomaly_detection.py` for better accuracy.
- **Update Training Data**: Incorporate new data to improve model performance.
- **Validate Models**: Test updated models to ensure they effectively identify anomalies.

## 🤝 Contributing

We welcome contributions from the community! To contribute:

1. **Fork the Repository**: Create a copy of the repository under your own GitHub account.
2. **Create a Feature Branch**: Use descriptive names for your branches (`git checkout -b feature/your-feature`).
3. **Make Your Changes**: Implement new features, bug fixes, or improvements.
4. **Commit Your Changes**: Commit with clear and detailed messages (`git commit -am 'Add feature X'`).
5. **Push Your Branch**: Push your changes to your forked repository (`git push origin feature/your-feature`).
6. **Open a Pull Request**: Submit a Pull Request to the main repository, describing your changes and their impact.

Please ensure your code adheres to the project's style guide and passes all tests

 before submitting a Pull Request.

## 🚀 Future Improvements

- **Enhanced Anomaly Detection**: Develop advanced ML models for better anomaly detection.
- **Improved UI/UX**: Revamp the web dashboard for a more intuitive user experience.
- **Extended Metrics**: Add support for additional metrics and services.
- **Scalability Enhancements**: Optimize the system for better performance and scalability.

## 🛠️ Troubleshooting

**Service Not Restarting**:
- Ensure that the `restart_service` function in `service_manager.py` is correctly implemented and has the necessary permissions.

**High CPU Usage Alerts**:
- Verify the CPU threshold settings in `config.json` or check the CPU monitoring logic in `adaptive_health_checks.py`.

**Distributed Monitoring Issues**:
- Confirm that server URLs in `config.json` are correct and that the monitored services are operational.

**Prometheus Metrics**:
- Check Prometheus configuration and ensure it is properly scraping metrics from the endpoint.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for your interest in the Self-Healing Server project! We appreciate your feedback and contributions. If you have any questions or need assistance, please open an issue or contact us via the repository.
