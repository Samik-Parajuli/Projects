[Uploading README.md…]()
# JSON Security Sanitizer & Formatter

![Python 3](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![RFC 8259](https://img.shields.io/badge/RFC-8259-green)
![Air Gapped](https://img.shields.io/badge/Security-Zero%20Egress-success)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

Air-gapped, zero-telemetry JSON validator, beautifier, and minifier engineered for security professionals handling confidential tokens, intercepted HTTP proxy streams, and API keys without leaking data to cloud formatters. Pinpoints exact syntax error positions (line and column numbers).

---

## Features

- **Zero Cloud Transmission**: Runs 100% locally in browser or CLI.
- **Line & Column Error Localization**: Quickly debugs truncated API payloads or broken JSON.
- **Beautify & Minify**: One-click formatting with 2-space indentation or ultra-compact single-line minification.

---

## Terminal CLI Usage

```bash
# Beautify a JSON file
python3 json_sanitizer.py dirty.json --beautify

# Minify a JSON payload
python3 json_sanitizer.py dirty.json --minify

# Validate JSON via piped stream
cat payload.json | python3 json_sanitizer.py --validate
```

---

## Author & License

Developed by **Sameek Parajuli** ([GitHub](https://github.com/Samik-Parajuli)).  
Released under the [MIT License](LICENSE).
