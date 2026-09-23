#!/usr/bin/env python3
"""
HTTP Security Header Scanner & Hardener
Author: Sameek Parajuli (https://github.com/Samik-Parajuli)
License: MIT
"""

import sys
import argparse
import urllib.request
import urllib.error

def audit_headers(headers_dict):
    score = 100
    audits = []

    # Case-insensitive map
    h = {k.lower(): v for k, v in headers_dict.items()}

    # CSP
    if 'content-security-policy' in h:
        audits.append(("[PASS]", "Content-Security-Policy", "Configured against XSS & injection."))
    else:
        score -= 25
        audits.append(("[FAIL]", "Content-Security-Policy", "Missing! Vulnerable to Cross-Site Scripting (XSS)."))

    # HSTS
    if 'strict-transport-security' in h:
        val = h['strict-transport-security'].lower()
        if 'max-age=' in val:
            audits.append(("[PASS]", "Strict-Transport-Security", f"Configured ({h['strict-transport-security']})."))
        else:
            score -= 10
            audits.append(("[WARN]", "Strict-Transport-Security", "HSTS present but missing valid max-age."))
    else:
        score -= 20
        audits.append(("[FAIL]", "Strict-Transport-Security", "Missing! Vulnerable to SSL-stripping & downgrade attacks."))

    # X-Frame-Options
    if 'x-frame-options' in h:
        xfo = h['x-frame-options'].upper()
        if xfo in ['DENY', 'SAMEORIGIN']:
            audits.append(("[PASS]", "X-Frame-Options", f"Clickjacking protection enabled ({xfo})."))
        else:
            audits.append(("[WARN]", "X-Frame-Options", f"Non-standard policy: {xfo}"))
    else:
        score -= 15
        audits.append(("[FAIL]", "X-Frame-Options", "Missing! Vulnerable to Clickjacking in iframes."))

    # X-Content-Type-Options
    if h.get('x-content-type-options', '').lower() == 'nosniff':
        audits.append(("[PASS]", "X-Content-Type-Options", "MIME sniffing protection active (nosniff)."))
    else:
        score -= 10
        audits.append(("[FAIL]", "X-Content-Type-Options", "Missing 'nosniff'. Browsers may execute text files as script."))

    # Referrer-Policy
    if 'referrer-policy' in h:
        audits.append(("[PASS]", "Referrer-Policy", f"Configured ({h['referrer-policy']})."))
    else:
        score -= 5
        audits.append(("[WARN]", "Referrer-Policy", "Missing. Referer URLs may leak sensitive tokens across origins."))

    # Information Disclosure
    if 'server' in h:
        score -= 5
        audits.append(("[WARN]", "Information Disclosure: Server", f"Leaking server banner: '{h['server']}'"))
    if 'x-powered-by' in h:
        score -= 10
        audits.append(("[FAIL]", "Information Disclosure: X-Powered-By", f"Leaking runtime banner: '{h['x-powered-by']}'"))

    score = max(0, min(100, score))
    grade = 'F'
    if score >= 90: grade = 'A+'
    elif score >= 80: grade = 'A'
    elif score >= 65: grade = 'B'
    elif score >= 50: grade = 'C'
    elif score >= 35: grade = 'D'

    print("=" * 60)
    print(f" [*] HTTP SECURITY HEADER AUDIT: GRADE {grade} ({score}/100)")
    print("=" * 60)
    for status, name, desc in audits:
        print(f" {status:<7} {name:<26} -> {desc}")

    print("\n" + "-" * 60)
    print(" [*] HARDENED NGINX CONFIGURATION SNIPPET:")
    print("-" * 60)
    print("""# Add to server {} block:
add_header X-Frame-Options "DENY" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
add_header Content-Security-Policy "default-src 'self'; script-src 'self'; object-src 'none';" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
server_tokens off;""")

def main():
    parser = argparse.ArgumentParser(description="HTTP Security Header Scanner")
    parser.add_argument("--url", "-u", help="Target URL to fetch and audit")
    parser.add_argument("--file", "-f", help="File containing raw headers")
    parser.add_argument("--sample", action="store_true", help="Audit sample vulnerable headers")
    args = parser.parse_args()

    headers = {}
    if args.url:
        req = urllib.request.Request(args.url, headers={'User-Agent': 'Mozilla/5.0 (Security-Header-Scanner)'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                headers = dict(response.headers)
        except Exception as e:
            print(f"[!] Error fetching URL: {e}", file=sys.stderr)
            sys.exit(1)
        audit_headers(headers)
    elif args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    k, v = line.split(':', 1)
                    headers[k.strip()] = v.strip()
        audit_headers(headers)
    elif args.sample:
        sample = {
            "Server": "Apache/2.4.41 (Ubuntu)",
            "X-Powered-By": "PHP/7.4.3",
            "Content-Type": "text/html; charset=UTF-8"
        }
        audit_headers(sample)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
