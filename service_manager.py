import os
import structlog

logger = structlog.get_logger()

class ServiceManager:
    def restart_service(self, service_name):
        try:
            os.system(f'systemctl restart {service_name}')
            logger.info(f"Restarted service: {service_name}")
        except Exception as e:
            logger.error(f"Failed to restart service: {service_name}", error=str(e))
