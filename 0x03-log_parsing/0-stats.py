#!/usr/bin/python3
"""
This script reads stdin line by line to output the statistics after
every 10 lines or on a keyboard interrupt
"""

import sys
import fileinput


def print_output(status_codes, file_size):
    """
    Prints the result in the required format
    """
    print(f"File size: {file_size}")
    status_codes = dict(sorted(status_codes.items()))

    for code, code_count in status_codes.items():
        print(f"{code}: {code_count}")


def get_log():
    """
    Gets the log from stdin
    """
    file_size = 0
    status_code = {}
    track_state = False
    try:
        counter = 0
        for lines in fileinput.input():
            try:
                lines = lines.rstrip("\n")
                new_list = lines.split()

                if len(new_list) != 9:
                    continue

                if not new_list[-1].isdigit() or not new_list[-2].isdigit():
                    track_state = True
                    continue

                file_size += int(new_list[-1])
                status_code[int(new_list[-2])] = status_code.get(
                                                int(new_list[-2]), 0) + 1

                counter += 1

                if counter % 10 == 0:
                    print_output(status_code, file_size)

            except Exception as e:
                raise ValueError(e)

        if track_state is True:
            raise ValueError("Not a digit")

    except (KeyboardInterrupt, Exception) as e:
        print_output(status_code, file_size)
        sys.stderr.write("[stderr]: {}\n".format(e))
        sys.exit(1)

    print_output(status_code, file_size)


if __name__ == '__main__':
    get_log()
