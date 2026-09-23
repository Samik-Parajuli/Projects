#!/usr/bin/env python3
"""
Cyber Regex Pattern & Artifact Extractor
Author: Sameek Parajuli (https://github.com/Samik-Parajuli)
License: MIT
"""

import sys
import re
import argparse
from collections import Counter

PATTERNS = {
    "ipv4": (r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', "IPv4 Addresses"),
    "md5": (r'\b[a-fA-F0-9]{32}\b', "MD5 Hashes"),
    "sha1": (r'\b[a-fA-F0-9]{40}\b', "SHA-1 Hashes"),
    "sha256": (r'\b[a-fA-F0-9]{64}\b', "SHA-256 Hashes"),
    "email": (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', "Email Addresses"),
    "jwt": (r'\beyJ[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*\b', "JWT Tokens"),
    "aws": (r'\bAKIA[0-9A-Z]{16}\b', "AWS Access Key IDs")
}

def extract_artifacts(text, pattern_keys=None):
    if not pattern_keys:
        pattern_keys = list(PATTERNS.keys())

    print("=" * 60)
    print(" [*] CYBER ARTIFACT & IOC EXTRACTION REPORT")
    print("=" * 60)

    total_found = 0
    for k in pattern_keys:
        if k not in PATTERNS: continue
        regex, label = PATTERNS[k]
        matches = re.findall(regex, text)
        if matches:
            counts = Counter(matches)
            print(f"\n[+] {label} ({len(counts)} unique, {len(matches)} total):")
            for item, count in counts.most_common(20):
                print(f"  -> {item} (x{count})")
            total_found += len(matches)

    if total_found == 0:
        print("[!] No artifacts detected matching requested patterns.")

def main():
    parser = argparse.ArgumentParser(description="Cyber Regex Pattern & Artifact Extractor")
    parser.add_argument("file", nargs="?", help="Log or text file to extract IOCs from")
    parser.add_argument("--type", "-t", default="all", help="Comma-separated types: ipv4,md5,sha1,sha256,email,jwt,aws,all")
    parser.add_argument("--sample", action="store_true", help="Extract from sample threat intelligence dump")
    args = parser.parse_args()

    types = list(PATTERNS.keys()) if args.type == "all" else args.type.split(',')

    if args.sample:
        sample = """
        [2026-08-14 02:15:33] Inbound connection from 192.168.1.105:44342 to 10.0.0.1:443
        Suspicious payload hash: 5d41402abc4b2a76b9719d911017c592
        SHA256: 2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
        Admin alert dispatched to secops@enterprise.corp
        AWS leaked token: AKIAIOSFODNN7EXAMPLE
        Token authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0In0.sample
        """
        extract_artifacts(sample, types)
    elif args.file:
        with open(args.file, 'r', encoding='utf-8', errors='ignore') as f:
            extract_artifacts(f.read(), types)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
