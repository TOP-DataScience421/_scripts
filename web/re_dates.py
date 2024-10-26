from pathlib import Path
from re import compile
from sys import path


pat_date = compile(
    r'((0[1-9]|1[0-9]|2[0-9]|3[01])'
    r'[/\.-]'
    r'(0[1-9]|1[012])'
    r'[/\.-]'
    r'(19\d\d|20\d\d))'
    r'|'
    r'((19\d\d|20\d\d)'
    r'[/\.-]'
    r'(0[1-9]|1[012])'
    r'[/\.-]'
    r'(0[1-9]|1[0-9]|2[0-9]|3[01]))'
)

test_text = (Path(path[0]) / 'date_formats.html').read_text()
dates = list(pat_date.finditer(test_text))

# >>> len(dates)
# 311



