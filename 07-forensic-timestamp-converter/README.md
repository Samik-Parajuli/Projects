[Uploading README.md…]()
# Forensic Timestamp & Active Directory Converter

![Python 3](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![DFIR](https://img.shields.io/badge/DFIR-Timeline%20Forensics-purple)
![FILETIME](https://img.shields.io/badge/Windows-FILETIME%201601-blue)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

Multi-standard forensic epoch converter built for digital forensics examiners and timeline analysts. Interconverts Unix Seconds, Milliseconds, ISO 8601, and Windows 64-bit FILETIME (100-nanosecond intervals since January 1, 1601) used in NTFS USN Journals (`$Extend\$J`), Registry timestamps, and Active Directory LDAP attributes (`pwdLastSet`, `badPasswordTime`).

---

## Features

- **Windows 64-bit FILETIME**: 100-nanosecond intervals since Jan 1, 1601 (NTFS, Registry, Active Directory).
- **Unix Epoch (Seconds & Milliseconds)**: Standard POSIX timestamps since Jan 1, 1970.
- **Bi-Directional Auto-Detection**: Enter either raw timestamps or human-readable dates.
- **UTC & Local Synchronization**: Eliminates timezone discrepancies in forensic timelines.

---

## Terminal CLI Usage

```bash
# Decode a Windows 64-bit FILETIME (e.g. from an NTFS USN Journal)
python3 timestamp_forensics.py 133698765430000000

# Decode a Unix Epoch timestamp
python3 timestamp_forensics.py 1726000000

# Convert ISO 8601 human date into forensic timestamps
python3 timestamp_forensics.py "2026-08-15 12:00:00"

# Print current time across all forensic standards
python3 timestamp_forensics.py --now
```

---

## Author & License

Developed by **Sameek Parajuli** ([GitHub](https://github.com/Samik-Parajuli)).  
Released under the [MIT License](LICENSE).
