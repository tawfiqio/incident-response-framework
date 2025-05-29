from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        dst_port = packet[TCP].dport

        if dst_port in [23, 445, 3389]:  # Flag Telnet, SMB, RDP activity
            print(f"⚠️ Suspicious traffic detected: {src_ip} -> {dst_ip}:{dst_port}")

sniff(prn=packet_callback, store=0, count=100)
