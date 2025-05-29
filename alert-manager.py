import smtplib

class AlertManager:
    def __init__(self, email, events):
        self.email = email
        self.events = events

    def send_alert(self):
        high_risk_events = [event for event, severity in self.events.items() if severity in ["High", "Critical"]]

        if not high_risk_events:
            return

        message = f"Subject: Security Alert\n\nHigh-Risk Threats Detected:\n" + "\n".join(high_risk_events)
        
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your_email@example.com", "your_password")
            server.sendmail("your_email@example.com", self.email, message)

        print("⚠️ High-Risk Alert Sent!")

if __name__ == "__main__":
    threats = {"Unauthorized access attempt": "High", "Malware detected": "Critical"}
    alert = AlertManager("security_team@example.com", threats)
    alert.send_alert()
