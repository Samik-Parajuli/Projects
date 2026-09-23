
[README.md](https://github.com/user-attachments/files/32566881/README.md)
# HTTP Security Header Scanner & Hardener

![Python 3](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![OWASP](https://img.shields.io/badge/OWASP-Top%2010-red)
![Defense-in-Depth](https://img.shields.io/badge/Security-A%2B%20Grading-success)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

Audits HTTP response headers against modern defense-in-depth guidelines (OWASP, NIST, MDN Web Docs). Evaluates CSP, HSTS, X-Frame-Options, X-Content-Type-Options, and Referrer-Policy, provides letter grades (A+ to F), detects information disclosure banners (`Server`, `X-Powered-By`), and automatically outputs production-ready Nginx and Apache hardening snippets.

---

## Features

- **Automated A+ to F Grading**: Weighted scoring algorithm based on vulnerability impact.
- **OWASP Header Validation**:
  - `Content-Security-Policy` (XSS & Injection mitigation)
  - `Strict-Transport-Security` (HSTS with max-age and preload verification)
  - `X-Frame-Options` (Clickjacking defense)
  - `X-Content-Type-Options` (MIME sniffing prevention)
  - `Referrer-Policy` (Data leakage prevention)
- **Information Disclosure Detection**: Identifies leaked server banners (`nginx/1.18.0`, `PHP/8.1`, `ASP.NET`).
- **Nginx / Apache Config Generator**: Instantly outputs copy-paste directives for production web servers.

---

## Terminal CLI Usage

```bash
# Audit a live web application
python3 header_scanner.py --url https://example.com

# Audit raw headers from a file
python3 header_scanner.py --file headers.txt

# Audit built-in sample
python3 header_scanner.py --sample
```

---

## Web Interface

Open `index.html` in any browser for real-time audit, instant preset tests, and checklist generation.

---

## Author & License

Developed by **Sameek Parajuli** ([GitHub](https://github.com/Samik-Parajuli)).  
Released under the [MIT License](LICENSE).
