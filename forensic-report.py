import json

class ForensicReport:
    def __init__(self, incidents):
        self.incidents = incidents

    def generate_report(self):
        report_data = {"Incidents": self.incidents}
        
        with open("forensic_report.json", "w") as file:
            json.dump(report_data, file, indent=4)
        
        print("📄 Forensic report saved as `forensic_report.json`")

if __name__ == "__main__":
    sample_incidents = {
        "Failed login attempt": "Low",
        "Malware execution detected": "Critical"
    }
    report = ForensicReport(sample_incidents)
    report.generate_report()
