from html.parser import HTMLParser
from pathlib import Path
from sys import path

script_dir = Path(path[0])
source_file = script_dir / 'python_html_parser.html'

html_doc = source_file.read_text(encoding='utf-8')


class Documentation(HTMLParser):
    
    append_data = False
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []
    
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section':
            if attrs['id'] == 'module-html.parser':
                self.append_data = True
    
    def handle_endtag(self, tag):
        if self.append_data:
            if tag == 'section':
                self.append_data = False
    
    def handle_data(self, data):
        if self.append_data:
            self.data.append(data)
    

parser = Documentation()
parser.feed(html_doc)

