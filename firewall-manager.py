import os

def block_ip(ip_address):
    print(f"⛔ Blocking IP: {ip_address}")
    os.system(f"iptables -A INPUT -s {ip_address} -j DROP")

if __name__ == "__main__":
    malicious_ips = ["192.168.1.100", "203.0.113.45"]
    for ip in malicious_ips:
        block_ip(ip)
