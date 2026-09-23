# Security Projects & Tactical Engineering Suite

![Cybersecurity](https://img.shields.io/badge/Security-Offensive%20%26%20DFIR-red)
![Author](https://img.shields.io/badge/Author-Sameek%20Parajuli-blue)
![Projects](https://img.shields.io/badge/Projects-8%20Standalones-success)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

A collection of **8 purpose-built, client-side offensive and forensic analysis applications** designed for penetration testers, security researchers, and incident responders. Built with **zero external telemetry, air-gapped data safety, and zero backend egress**.

Every project in this directory is a **self-contained standalone module** with:
1. A **CLI utility in Python 3** (standard library only, 0 dependencies).
2. A **modern web application** with dark tactical UI (HTML5 / CSS / Vanilla JS).
3. Comprehensive **documentation and MIT license**.

---

## Project Directory Matrix

| # | Project Directory | Domain | Primary Technical Capability | CLI Utility |
|---|---|---|---|---|
| **01** | [`01-jwt-security-analyzer`](./01-jwt-security-analyzer) | Auth & Crypto | RFC 7519 decoding, token expiration checks, `alg: none` (CVE-2015-9235) exploit testing | `jwt_tool.py` |
| **02** | [`02-http-security-header-scanner`](./02-http-security-header-scanner) | AppSec & Hardening | Live A+ to F security grading, OWASP headers audit, Nginx/Apache config generator | `header_scanner.py` |
| **03** | [`03-cidr-subnet-calculator`](./03-cidr-subnet-calculator) | Network & Infra | 32-bit bitwise IPv4 subnet math, host range mapping, RFC 1918 scope, binary octets | `cidr_calc.py` |
| **04** | [`04-cve-intelligence-radar`](./04-cve-intelligence-radar) | Threat Intel | Weaponized CVE lookup (Log4Shell, EternalBlue, ProxyLogon, XZ), CVSS v3.1, PoCs | `cve_radar.py` |
| **05** | [`05-subdomain-url-ssrf-parser`](./05-subdomain-url-ssrf-parser) | AppSec & Recon | RFC 3986 URL deconstruction, subdomain hierarchies, SSRF cloud metadata mutations | `url_parser.py` |
| **06** | [`06-cyber-regex-artifact-extractor`](./06-cyber-regex-artifact-extractor) | DFIR & Triage | IOC carving (IPv4, MD5/SHA, JWT, AWS keys) from unstructured logs with frequency counting | `ioc_extractor.py` |
| **07** | [`07-forensic-timestamp-converter`](./07-forensic-timestamp-converter) | Timeline Forensics | Windows 64-bit FILETIME (AD 1601 / NTFS USN Journal) & Unix Epoch bi-directional sync | `timestamp_forensics.py` |
| **08** | [`08-json-security-sanitizer`](./08-json-security-sanitizer) | Data Sanitization | Air-gapped JSON validator, 2-space beautifier, minifier, line/col syntax diagnostics | `json_sanitizer.py` |

---

## Author

**Sameek Parajuli**  
- **GitHub**: [github.com/Samik-Parajuli](https://github.com/Samik-Parajuli)  
- **Focus**: Offensive Security, Black-Box Web App Penetration Testing, DFIR  
- **TryHackMe**: [#1 Sapphire & Ruby Leagues](https://tryhackme.com/p/sameekey)
