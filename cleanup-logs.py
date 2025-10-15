#!/usr/bin/env python3
"""
Linux Log Cleanup Automation Tool
Author: AJAY KORIVI
"""

import os
import argparse
from datetime import datetime, timedelta

def cleanup_logs(directory, days):
    cutoff = datetime.now() - timedelta(days=days)
    deleted_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_mtime < cutoff:
                    os.remove(file_path)
                    deleted_files.append(file_path)

    if deleted_files:
        print(f"Deleted {len(deleted_files)} log files:")
        for f in deleted_files:
            print(f" - {f}")
    else:
        print("No old log files to delete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleanup old log files in a directory")
    parser.add_argument("-d", "--directory", required=True, help="Directory to scan")
    parser.add_argument("-t", "--days", type=int, default=30, help="Delete logs older than DAYS (default 30)")
    args = parser.parse_args()

    cleanup_logs(args.directory, args.days)
