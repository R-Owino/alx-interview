#!/usr/bin/python3
"""
This script reads stdin line by line to output the statistics after
every 10 lines or on a keyboard interrupt
"""

import sys
import re
from collections import defaultdict
import signal
from typing import Tuple, Optional, Dict


def parse_log_line(line: str) -> Optional[Tuple[str, str, int, int]]:
    """
    Parse a log line and extract relevant information.

    Args:
        line (str): A log line in the specified format.

    Returns:
        Optional[Tuple[str, str, int, int]]: A tuple containing IP address,
        date, status code, and file size, or None if the format doesn't match
    """
    pattern = (
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
        r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None


def print_metrics(total_size: int, status_code_counts: Dict[int, int]) -> None:
    """
    Print computed statistics based on total file size and status code counts.

    Args:
        total_size (int): Total file size.
        status_code_counts (Dict[int, int]): dictionary containing status code
        counts.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")


def signal_handler(sig: int, frame) -> None:
    """
    Handle KeyboardInterrupt to print metrics and exit

    Args:
        sig (int): Signal number.
        frame: Current stack frame.
    """
    print_metrics(total_size, status_code_counts)
    sys.exit(0)


total_size = 0
status_code_counts = defaultdict(int)
line_count = 0

# Set up the KeyboardInterrupt (CTRL+C) signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        parsed_data = parse_log_line(line)
        if parsed_data:
            ip, date, status_code, file_size = parsed_data
            total_size += int(file_size)
            status_code_counts[int(status_code)] += 1
            line_count += 1

        if line_count % 10 == 0:
            print_metrics(total_size, status_code_counts)

except KeyboardInterrupt:
    # Handle the case where the user interrupts the script with CTRL+C
    print_metrics(total_size, status_code_counts)
    sys.exit(0)
