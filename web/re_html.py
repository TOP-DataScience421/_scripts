from pathlib import Path
from re import compile, DOTALL
from sys import path


text_par = compile(
    r'<p>(.*?)</p>',
   DOTALL
)

test_text = (Path(path[0]) / 'date_formats.html').read_text()
paragraphs = list(text_par.finditer(test_text))

# >>> len(dates)
# 311



