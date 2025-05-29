import re

class LogParser:
    def __init__(self, log_file):
        self.log_file = log_file

    def detect_threats(self):
        with open(self.log_file, "r") as file:
            logs = file.readlines()
        
        suspicious_events = []
        
        for log in logs:
            if re.search(r"(failed login|unauthorized access)", log, re.IGNORECASE):
                suspicious_events.append(log.strip())
        
        return suspicious_events

if __name__ == "__main__":
    parser = LogParser("system_logs.txt")
    threats = parser.detect_threats()
    print(f"Potential Threats Detected:\n{threats}")
