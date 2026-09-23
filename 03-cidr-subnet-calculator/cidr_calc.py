#!/usr/bin/env python3
"""
CIDR / IP Subnet Calculator & Range Engine
Author: Sameek Parajuli (https://github.com/Samik-Parajuli)
License: MIT
"""

import sys
import argparse
import ipaddress

def to_bin(ip_int):
    b = f"{ip_int:032b}"
    return f"{b[0:8]}.{b[8:16]}.{b[16:24]}.{b[24:32]}"

def calculate_cidr(cidr_str):
    try:
        network = ipaddress.IPv4Network(cidr_str, strict=False)
    except Exception as e:
        print(f"[!] Invalid CIDR expression '{cidr_str}': {e}", file=sys.stderr)
        return False

    net_addr = network.network_address
    bcast_addr = network.broadcast_address
    netmask = network.netmask
    wildcard = ipaddress.IPv4Address(int(network.hostmask))
    total_hosts = network.num_addresses
    usable_hosts = max(0, total_hosts - 2) if network.prefixlen < 31 else (2 if network.prefixlen == 31 else 1)

    first_host = ipaddress.IPv4Address(int(net_addr) + 1) if network.prefixlen < 31 else net_addr
    last_host = ipaddress.IPv4Address(int(bcast_addr) - 1) if network.prefixlen < 31 else bcast_addr

    scope = "Public Internet"
    if network.is_private:
        scope = "RFC 1918 Private Network"
    elif network.is_loopback:
        scope = "RFC 1122 Loopback"
    elif network.is_link_local:
        scope = "RFC 3927 Link-Local (APIPA)"

    print("=" * 60)
    print(f" [*] CIDR SUBNET CALCULATION: {network}")
    print("=" * 60)
    print(f"  Network Address    : {net_addr}")
    print(f"  Broadcast Address  : {bcast_addr}")
    print(f"  Subnet Netmask     : {netmask} (/{network.prefixlen})")
    print(f"  Wildcard Mask      : {wildcard}")
    print(f"  First Usable Host  : {first_host}")
    print(f"  Last Usable Host   : {last_host}")
    print(f"  Usable Host Range  : {first_host} - {last_host}")
    print(f"  Total Usable Hosts : {usable_hosts:,} (Total IPs: {total_hosts:,})")
    print(f"  Routing Scope      : {scope}")
    print("-" * 60)
    print(f"  Binary Netmask     : {to_bin(int(netmask))}")
    print(f"  Binary Network ID  : {to_bin(int(net_addr))}")
    return True

def main():
    parser = argparse.ArgumentParser(description="CIDR / IP Subnet Calculator")
    parser.add_argument("network", nargs="?", default="192.168.1.1/24", help="CIDR or IP network (e.g. 10.0.0.1/16)")
    parser.add_argument("--subnets", nargs=2, metavar=("NET", "NEW_PREFIX"), help="Subnet a network into smaller chunks")
    args = parser.parse_args()

    if args.subnets:
        net, p = args.subnets
        prefix = int(p.replace('/', ''))
        parent = ipaddress.IPv4Network(net, strict=False)
        print(f"[*] Subnetting {parent} into /{prefix} subnets:")
        for s in list(parent.subnets(new_prefix=prefix))[:16]:
            print(f"  -> {s}")
    else:
        calculate_cidr(args.network)

if __name__ == "__main__":
    main()
