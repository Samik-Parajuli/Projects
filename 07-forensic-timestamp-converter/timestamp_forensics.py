#!/usr/bin/env python3
"""
Forensic Timestamp & Active Directory Converter
Author: Sameek Parajuli (https://github.com/Samik-Parajuli)
License: MIT
"""

import sys
import argparse
from datetime import datetime, timezone

WINDOWS_EPOCH_DIFF = 11644473600

def filetime_to_dt(filetime_int):
    unix_secs = (filetime_int / 10000000) - WINDOWS_EPOCH_DIFF
    return datetime.fromtimestamp(unix_secs, tz=timezone.utc)

def dt_to_filetime(dt_obj):
    unix_secs = dt_obj.timestamp()
    return int((unix_secs + WINDOWS_EPOCH_DIFF) * 10000000)

def convert_timestamp(input_val):
    val_str = str(input_val).strip()
    dt = None

    if val_str.isdigit():
        num = int(val_str)
        if num > 1000000000000000: # FILETIME
            dt = filetime_to_dt(num)
        elif num > 10000000000: # Unix ms
            dt = datetime.fromtimestamp(num / 1000, tz=timezone.utc)
        else: # Unix secs
            dt = datetime.fromtimestamp(num, tz=timezone.utc)
    else:
        for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d'):
            try:
                dt = datetime.strptime(val_str, fmt).replace(tzinfo=timezone.utc)
                break
            except ValueError:
                pass

    if not dt:
        print(f"[!] Unrecognized date/timestamp format: {val_str}", file=sys.stderr)
        return False

    unix_s = int(dt.timestamp())
    unix_ms = int(dt.timestamp() * 1000)
    filetime = dt_to_filetime(dt)

    print("=" * 60)
    print(" [*] FORENSIC TIMESTAMP CONVERSION REPORT")
    print("=" * 60)
    print(f"  UTC Standard Time     : {dt.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"  ISO 8601 String       : {dt.isoformat()}")
    print(f"  Unix Epoch (Seconds)  : {unix_s}")
    print(f"  Unix Epoch (Millis)   : {unix_ms}")
    print(f"  Windows 64-bit FILETIME: {filetime} (Active Directory / NTFS)")
    print("=" * 60)
    return True

def main():
    parser = argparse.ArgumentParser(description="Forensic Timestamp Converter")
    parser.add_argument("timestamp", nargs="?", help="Timestamp or date string")
    parser.add_argument("--now", action="store_true", help="Print current time across all formats")
    args = parser.parse_args()

    if args.now:
        convert_timestamp(int(datetime.now(timezone.utc).timestamp()))
    elif args.timestamp:
        convert_timestamp(args.timestamp)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
