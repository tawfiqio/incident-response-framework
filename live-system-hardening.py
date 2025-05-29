import os
import subprocess

class SystemHardener:
    def __init__(self):
        self.security_measures = [
            ("🔒 Disabling unnecessary services", "systemctl stop bluetooth"),
            ("🚫 Blocking external scripts execution", "chmod -R -x /tmp"),
            ("⛔ Enforcing strong password policies", "sed -i 's/PASS_MAX_DAYS 99999/PASS_MAX_DAYS 90/' /etc/login.defs"),
            ("🔍 Configuring network firewall", "iptables -A INPUT -p tcp --dport 22 -j DROP"),
            ("⚡ Enabling audit logging", "auditctl -e 1"),
            ("🚀 Enforcing memory protection", "sysctl -w kernel.randomize_va_space=2"),
            ("🛡️ Blocking USB device execution", "echo 'blacklist usb-storage' >> /etc/modprobe.d/blacklist.conf"),
            ("⚠️ Locking down kernel settings", "sysctl -w net.ipv4.conf.default.rp_filter=1"),
        ]
    
    def harden_system(self):
        print("🚀 Applying Live System Hardening...")
        for desc, command in self.security_measures:
            print(f"{desc}...")
            subprocess.run(command, shell=True)
        print("✅ System Hardening Complete!")

if __name__ == "__main__":
    hardener = SystemHardener()
    hardener.harden_system()
