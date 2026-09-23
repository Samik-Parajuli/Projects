#!/usr/bin/env python3
"""
JSON Security Sanitizer & Formatter
Author: Sameek Parajuli (https://github.com/Samik-Parajuli)
License: MIT
"""

import sys
import json
import argparse

def process_json(raw_text, mode="beautify"):
    try:
        data = json.loads(raw_text)
        if mode == "minify":
            print(json.dumps(data, separators=(',', ':')))
        elif mode == "validate":
            print("[+] JSON is valid RFC 8259 syntax.")
        else:
            print(json.dumps(data, indent=2))
        return True
    except json.JSONDecodeError as e:
        print(f"[!] Invalid JSON Syntax:", file=sys.stderr)
        print(f"    Line {e.lineno}, Column {e.colno} (Char {e.pos})", file=sys.stderr)
        print(f"    Error: {e.msg}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="JSON Security Sanitizer")
    parser.add_argument("file", nargs="?", help="JSON file to process (reads stdin if omitted)")
    parser.add_argument("--beautify", action="store_true", help="Format JSON with 2-space indent")
    parser.add_argument("--minify", action="store_true", help="Compact JSON onto a single line")
    parser.add_argument("--validate", action="store_true", help="Validate JSON syntax without printing payload")
    args = parser.parse_args()

    mode = "minify" if args.minify else ("validate" if args.validate else "beautify")

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            process_json(f.read(), mode)
    elif not sys.stdin.isatty():
        process_json(sys.stdin.read(), mode)
    else:
        sample = '{"status":"ok","exploit":"cwe-362","threads":16,"targets":["admin","api"]}'
        print("[*] Sample formatted JSON:")
        process_json(sample, mode)

if __name__ == "__main__":
    main()
