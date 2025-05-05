from sniffer import capture_packets
from analyzer import analyze_packet

def main():
print("Network Packet Analyzer")
interface = input("Enter the interface (e.g., eth0, wlan0): ")
try:
count = int(input("Number of packets to capture: "))
except ValueError:
print("Invalid count. Defaulting to 10 packets.")
count = 10

    capture_packets(interface=interface, packet_count=count, callback=analyze_packet)

if **name** == "**main**":
main()
