[Uploading README.md…]()
# Subdomain & URL SSRF/Open-Redirect Parser

![Python 3](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![RFC 3986](https://img.shields.io/badge/RFC-3986-green)
![SSRF Radar](https://img.shields.io/badge/AppSec-SSRF%20Auditor-red)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

Offensive URL disassembly and parameter auditor designed for bug bounty recon, Server-Side Request Forgery (SSRF) payload construction, and open-redirect testing. Deconstructs URLs according to RFC 3986, maps subdomain hierarchies, and isolates query parameters with cloud metadata mutation injection presets.

---

## Features

- **RFC 3986 URL Disassembly**: Separates protocol, credentials, hostname, port, subdomain chain, path, query, and fragments.
- **SSRF Risk Evaluation**: Flags sensitive parameters (`url`, `redirect`, `dest`, `next`, `callback`, `target`).
- **Cloud Metadata Presets**:
  - AWS EC2 IMDSv1 (`http://169.254.169.254/latest/meta-data/`)
  - Google Cloud Metadata (`http://metadata.google.internal/`)
  - Azure Instance Metadata (`http://169.254.169.254/metadata/instance`)

---

## Terminal CLI Usage

```bash
# Audit a target URL
python3 url_parser.py "https://api.dev.target.com:8443/auth/callback?redirect=http://evil.com&token=xyz#debug"

# Generate SSRF cloud metadata mutation payloads
python3 url_parser.py "https://target.com/fetch?url=image.png" --ssrf-mutations
```

---

## Author & License

Developed by **Sameek Parajuli** ([GitHub](https://github.com/Samik-Parajuli)).  
Released under the [MIT License](LICENSE).
