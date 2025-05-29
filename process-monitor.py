import psutil

SUSPICIOUS_PROCESSES = ["nc.exe", "mimikatz.exe", "powershell.exe -nop"]

def monitor_processes():
    print("🔍 Monitoring running processes...")
    
    for process in psutil.process_iter(attrs=['pid', 'name']):
        process_name = process.info['name']
        
        for bad_proc in SUSPICIOUS_PROCESSES:
            if bad_proc.lower() in process_name.lower():
                print(f"🚨 ALERT: Suspicious Process Detected -> {process_name} (PID: {process.info['pid']})")

if __name__ == "__main__":
    monitor_processes()
