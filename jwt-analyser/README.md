[README.md](https://github.com/user-attachments/files/32566768/README.md)[Upload# JWT Security Analyzer & Token Auditor

![Python 3](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![RFC 7519](https://img.shields.io/badge/RFC-7519-green)
![Zero Telemetry](https://img.shields.io/badge/Security-Air--Gapped-success)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

A production-grade, client-side and terminal security auditor for JSON Web Tokens (RFC 7519). Decodes header, payload, and signature components, validates temporal expiration claims, and audits tokens for dangerous vulnerabilities including the **CVE-2015-9235 `alg: none` signature verification bypass attack** and stripped HMAC keys.

---

## Key Features

- **Base64URL Decoding**: Fully compliant URL-safe Base64 parser with automated padding resolution.
- **CVE-2015-9235 Vulnerability Testing**: Mutates any valid token to `alg: none` with a stripped signature for authentication bypass verification.
- **Timestamp & Expiration Audit**: Real-time evaluation of `exp`, `nbf`, and `iat` claims with human-readable countdowns and epoch translation.
- **Dual Mode**:
  - **CLI Utility**: Lightweight, zero-dependency Python 3 tool for terminal workflows.
  - **Web Application**: Beautiful, standalone dark-themed interactive workstation with live preview and syntax coloring.
- **100% Air-Gapped**: Runs entirely local with zero network calls, preventing secret token leakage.

---

## Terminal CLI Usage

```bash
# Inspect and audit a token
python3 jwt_tool.py --token "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Execute alg: 'none' signature bypass mutation
python3 jwt_tool.py --token "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." --none-attack

# Run audit on built-in security test sample
python3 jwt_tool.py --sample
```

---

## Web Interface

Simply open `index.html` in any modern browser:
```bash
# Linux / Kali
xdg-open index.html

# macOS
open index.html
```

---

## Author & License

Developed by **Sameek Parajuli** ([GitHub](https://github.com/Samik-Parajuli)).  
Released under the [MIT License](LICENSE).
ing README.md…]()
