#!/bin/bash

echo "🚀 Setting up Live System Hardening framework..."

# Install dependencies
pip install -r requirements.txt

# Enable audit logging
auditctl -e 1

# Configure firewall (modify rules as needed)
iptables -A INPUT -p tcp --dport 22 -j DROP  # Block SSH access

# Disable USB storage execution
echo 'blacklist usb-storage' | tee -a /etc/modprobe.d/blacklist.conf

# Harden kernel settings
sysctl -w kernel.randomize_va_space=2
sysctl -w net.ipv4.conf.all.rp_filter=1

# Enforce strict password policies
sed -i 's/PASS_MAX_DAYS 99999/PASS_MAX_DAYS 90/' /etc/login.defs

echo "✅ System Hardening Complete! Security settings applied."
