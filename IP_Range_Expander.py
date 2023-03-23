import ipaddress
import pandas as pd

def expand_ip_range(ip_range):
    # Split the IP range string into two parts
    start_ip, end_ip = ip_range.split('-')

    # Convert the start and end IP addresses to IPv4Address objects
    start_ip = ipaddress.IPv4Address(start_ip.strip())
    end_ip = ipaddress.IPv4Address(end_ip.strip())

    # Create a list of all IP addresses in the range
    ip_list = []
    for ip in range(int(start_ip), int(end_ip) + 1):
        ip_list.append(str(ipaddress.IPv4Address(ip)))
    return ip_list

ip_ranges = ["a.a.a.a.-a.a.a.d","c.c.c.c-c.c.c.f".....]
#output is a.a.a.a, a.a.a.b, a.a.a.c, a.a.a.d, c.c.c.c, c.c.c.d, c.c.c.e, c.c.c.f

ip_list = []

for ip_range in ip_ranges:
    ip_list.extend(expand_ip_range(ip_range))

for i in ip_list:
    print(str(i))
