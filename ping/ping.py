import argparse
from scapy.all import *

def ping(host, count):
    try:
        for _ in range(count):
            # Send an ICMP Echo Request and receive an ICMP Echo Reply
            response = sr1(IP(dst=host)/ICMP(), timeout=2, verbose=0)

            if response:
                print(f"Ping to {host} succeeded. Response time: {response.time * 1000:.2f} ms")
            else:
                print(f"Ping to {host} failed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Ping utility using Scapy.")
    parser.add_argument("host", help="Hostname or IP address to ping")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of pings to send (default is 1)")
    args = parser.parse_args()

    target_host = args.host
    ping(target_host, args.count)

if __name__ == "__main__":
    main()
