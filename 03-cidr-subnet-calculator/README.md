# CIDR / IP Subnet Calculator & Range Engine

![Python 3](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![RFC 1918](https://img.shields.io/badge/RFC-1918-green)
![Bitwise Math](https://img.shields.io/badge/Engine-32--Bit%20Binary-success)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

High-performance IPv4 bitwise calculation engine for penetration testers, security operations (SOC), and network architects. Instant computation of network address, broadcast address, subnet mask, wildcard mask, first and last usable host ranges, total usable IPs, binary representations, and RFC 1918 routing scope.

---

## Features

- **32-Bit Bitwise Math**: Accurate host range & boundary evaluation down to /30 and /32 single host pointers.
- **RFC 1918 Scope**: Identifies Private (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), Loopback, Link-Local, and Public routable IPs.
- **Binary Network Map**: Complete 32-bit binary network & host octet representation.
- **Subnet Carving**: List subnets and host partitions from larger supernets.

---

## Terminal CLI Usage

```bash
# Calculate IPv4 subnet
python3 cidr_calc.py 192.168.1.50/24

# Supports separate IP and Netmask
python3 cidr_calc.py 10.0.0.1 255.255.0.0

# Split a network into smaller /28 subnets
python3 cidr_calc.py --subnets 10.10.10.0/24 /28
```

---

## Author & License

Developed by **Sameek Parajuli** ([GitHub](https://github.com/Samik-Parajuli)).  
Released under the [MIT License](LICENSE).
