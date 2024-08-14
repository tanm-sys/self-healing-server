import smtplib
from email.mime.text import MIMEText

class AlertManager:
    def __init__(self, alert_email):
        self.alert_email = alert_email

    def send_alert(self, message):
        msg = MIMEText(message)
        msg['Subject'] = 'Self-Healing Server Alert'
        msg['From'] = 'no-reply@selfhealingserver.com'
        msg['To'] = self.alert_email

        with smtplib.SMTP('localhost') as server:
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
