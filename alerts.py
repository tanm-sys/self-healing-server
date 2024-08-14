import smtplib
from email.mime.text import MIMEText
import structlog

logger = structlog.get_logger()

class AlertManager:
    def __init__(self, alert_email):
        self.alert_email = alert_email

    def send_alert(self, message):
        try:
            msg = MIMEText(message)
            msg['Subject'] = 'Self-Healing Server Alert'
            msg['From'] = 'no-reply@selfhealingserver.com'
            msg['To'] = self.alert_email

            with smtplib.SMTP('localhost') as server:
                server.sendmail(msg['From'], [msg['To']], msg.as_string())
        except Exception as e:
            logger.error("Failed to send alert", error=str(e))
