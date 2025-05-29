import os

class ResponseActions:
    def __init__(self, threats):
        self.threats = threats

    def take_action(self):
        for event, severity in self.threats.items():
            if severity == "Critical":
                print(f"🚨 Taking action against: {event}")
                # Example: Blocking an IP or terminating a process
                os.system("iptables -A INPUT -s 192.168.1.10 -j DROP")  # Block malicious IP
                os.system("pkill malware_process")  # Kill malware process

if __name__ == "__main__":
    threats = {"Malware detected": "Critical"}
    responder = ResponseActions(threats)
    responder.take_action()
