#!/usr/bin/env python3
import os
import re
import sys

path = sys.argv[1]
files = os.listdir(path)

for file in files:
    filename = f"{path}/{file}"
    with open(filename, "r") as f:
        content = f.read()

    content = content.replace(
        "END:VEVENT", "X-MICROSOFT-CDO-BUSYSTATUS:OOF\nEND:VEVENT"
    )
    content = re.sub(r"SUMMARY:(.*)", r"SUMMARY:Public holiday(\1)", content)

    with open(filename, "w") as f:
        f.write(content)
