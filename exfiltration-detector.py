import psutil

def detect_exfiltration(threshold_mb=100):
    print("🔍 Monitoring network activity for large transfers...")

    for conn in psutil.net_connections():
        if conn.status == 'ESTABLISHED' and conn.raddr:
            bytes_sent = conn.fd  # Simulated data usage (modify as needed)

            if bytes_sent / (1024 * 1024) > threshold_mb:
                print(f"🚨 ALERT: Possible Exfiltration Detected! {bytes_sent / (1024 * 1024)} MB transferred.")

if __name__ == "__main__":
    detect_exfiltration()
