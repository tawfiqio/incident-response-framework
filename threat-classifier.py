class ThreatClassifier:
    def __init__(self, events):
        self.events = events

    def classify(self):
        severity_map = {
            "failed login": "Low",
            "unauthorized access": "High",
            "malware detected": "Critical"
        }
        
        classified_events = {}
        
        for event in self.events:
            for keyword, severity in severity_map.items():
                if keyword in event.lower():
                    classified_events[event] = severity
        
        return classified_events

if __name__ == "__main__":
    raw_events = ["Unauthorized access attempt", "Failed login from IP 192.168.1.10", "Malware detected on server"]
    classifier = ThreatClassifier(raw_events)
    classified = classifier.classify()
    print("Classified Threats:", classified)
