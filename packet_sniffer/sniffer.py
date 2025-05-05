from scapy.all import sniff

def capture_packets(interface="eth0", packet_count=10, callback=None):
    print(f"Capturing {packet_count} packets on interface {interface}...")
    sniff(iface=interface, prn=callback, count=packet_count, store=False)
