# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import os
import sys
import select
import fileinput
import argparse
import syslog
from .config import Config
from .main import machina


def options_and_arguments():
    parser = argparse.ArgumentParser(
        description="Machina-Ratiocinatrix ratiocinates.",
        epilog="Example:  machina input_text.txt > output_text.txt"
    )

    parser.add_argument('-a', '--append',
                        action='store_true',
                        help="Append the proceeds to the input.")

    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help="Debug flag.")

    parser.add_argument('-i', '--interactive',
                        action='store_true',
                        help="Enable interactive mode (defaults to False)")

    # Positional arguments (files)
    # '*' captures zero or more arguments into a list, nargs='+' one or more.
    parser.add_argument('filenames',
                        nargs='*',
                        help="Zero (when text comes though a pipe) or more files to process.")
    return parser


def run():
    """After installation, on Linux prompt
    $ machina file1.txt file2.txt > output.txt
    """
    args = options_and_arguments().parse_args()

    # If no files are provided AND no data is being piped in - exit.
    if not args.filenames:
        # Check if stdin (fd 0) is ready to be read
        readable, _, _ = select.select([sys.stdin], [], [], 0.1)
        if not readable:
            print("Error: No input files or piped text stream.")
            options_and_arguments().print_help()
            sys.exit(1)

    # Ingest files line by line. Join is here for long files.
    lines = []
    for line in fileinput.input(files=args.filenames or ['-'], encoding="utf-8"):
        lines.append(line)
    raw_input = "".join(lines)

    config = Config()

    try:
        utterance = "Machina is ready"
        # Open syslog connection
        syslog.openlog(
            ident="machina-ratiocinatrix",
            logoption=syslog.LOG_NDELAY,
            facility=syslog.LOG_USER
        )
        # Signal (single line less than 4096 only!)
        syslog.syslog(syslog.LOG_INFO, utterance)
        syslog.closelog()

    except Exception as e:
        if args.debug:
            import traceback
            traceback.print_exc()
        else:
            sys.stderr.write(f'Machina did not work {e}\n')
            sys.stderr.flush()
        sys.exit(1)


if __name__ == '__main__':
    run()
