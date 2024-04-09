#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse
from pathlib import Path

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    try:
        year = re.search(r"(\d){4}", filename).group(0)
    except Exception:
        sys.exit("Error in parsing the year from file name.")
    with open(Path.cwd().joinpath(filename), "r") as file:
        # print(file.readlines()) # Extract all the text
        lines = file.readlines()
        file_content = "".join(lines)
        matches = re.findall(
            r'<tr align="right"><td>(\d{1,4})</td><td>([a-zA-Z]{1,})</td><td>([a-zA-Z]{1,})</td>',
            file_content,
        )
    print(matches)

    return


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print("usage: [--summaryfile] file [file ...]")
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == "--summaryfile":
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    parser = argparse.ArgumentParser(description="Process some babynames file.")
    parser.add_argument(
        "-f",
        "--file-name-list",
        default=[],
        nargs="+",
        help="File name list, all files with .html extension",
    )

    args = parser.parse_args()

    if args.file_name_list is []:
        print(
            "Please add the file name list as arguments. Usage: python babynames.py -f baby1990.html baby1992.html"
        )
        sys.exit(0)
    for file_name in args.file_name_list:
        extract_names(file_name)


if __name__ == "__main__":
    main()
