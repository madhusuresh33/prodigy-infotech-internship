from scapy.layers.inet import IP, TCP, UDP, ICMP

def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = "Unknown"
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"

        print(f"Source IP: {ip_layer.src} --> Destination IP: {ip_layer.dst}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {bytes(packet[IP].payload)[:30]}...\n")
