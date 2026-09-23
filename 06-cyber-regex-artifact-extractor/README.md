[Uploading README.md…]()
# Cyber Regex Pattern & Artifact Extractor

![Python 3](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![PCRE](https://img.shields.io/badge/Regex-PCRE%20Triage-green)
![DFIR IOCs](https://img.shields.io/badge/Forensics-IOC%20Deduplication-blue)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

Digital forensics and incident response (DFIR) triage tool for automated extraction and deduplication of Indicators of Compromise (IOCs) from unstructured text, memory strings, pcap logs, and code. Features security-optimized regex patterns for IPv4 addresses, cryptographic hashes, email addresses, JWT tokens, and cloud access keys.

---

## Supported Artifact Presets

- **IPv4 Addresses**: Bounded octet regex (`0-255`)
- **Cryptographic Hashes**: MD5 (32-hex), SHA-1 (40-hex), SHA-256 (64-hex)
- **Authentication Tokens**: JSON Web Tokens (`ey...`)
- **Cloud Credentials**: AWS Access Key IDs (`AKIA[0-9A-Z]{16}`)
- **Email Addresses**: RFC 5322 compliance

---

## Terminal CLI Usage

```bash
# Extract all artifacts from log file
python3 ioc_extractor.py sample.log --type all

# Extract specific artifact classes
python3 ioc_extractor.py dump.txt --type ip,hashes,aws

# Run on built-in security threat sample
python3 ioc_extractor.py --sample
```

---

## Author & License

Developed by **Sameek Parajuli** ([GitHub](https://github.com/Samik-Parajuli)).  
Released under the [MIT License](LICENSE).
