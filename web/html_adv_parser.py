from html.parser import HTMLParser
from pathlib import Path
from re import compile
from sys import path

script_dir = Path(path[0])
source_file = script_dir / 'python_html_parser.html'
edited_file = script_dir / 'python_html_parser_ed.html'

html_doc = source_file.read_text(encoding='utf-8')


flat_tags = [
    'br',
    'hr',
    'img',
    'input',
    'link',
    'meta',
    'option',
    'script',
]
empty_tags = [
    'area',
    'base',
    'br',
    'col',
    'embed',
    'hr',
    'img',
    'input',
    'keygen',
    'link',
    'meta',
    'param',
    'source',
    'track',
    'wbr'
]


class HTMLTag(list):
    indent = 2
    
    def __init__(self, tag, attrs, parent=None):
        # breakpoint()
        self.name = tag
        self.attrs = dict(attrs)
        self.data = ''
        self.parent = parent
        if parent is not None:
            parent.append(self)
    
    def iter_all(self):
        res = list(self)
        for ch in self:
            res.extend(ch.iter_all())
        return res
    
    def get_tag(self, tag_name, **attrs):
        result = []
        for ch in self:
            if ch.name == tag_name:
                if set(attrs.items()) <= set(ch.attrs.items()):
                    result.append(ch)
            result.extend(ch.get_tag(tag_name, **attrs))
        return result
    
    def __repr__(self):
        return f'<{self.name}>'
    
    def _str(self, lvl=0):
        indent = ' ' * self.indent * lvl
        attrs = ' '.join([
            f'{k}="{v}"'
            for k, v in self.attrs.items()
        ])
        attrs = " " + attrs if attrs else ""
        res = f'{indent}<{self.name}{attrs}>{self.data or ""}\n'
        for child in self:
            res += child._str(lvl+1)
        if self.name not in empty_tags:
            res += f'{indent}</{self.name}>\n'
        return res
    
    def __str__(self):
        return self._str()


class Documentation(HTMLParser):
    pat_whitespaces = compile(r'\s+')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = None
        self.last_parent = None
        self.last_tag = None
        
    def feed(self, data):
        data = self.pat_whitespaces.sub(' ', data)
        super().feed(data)

    def handle_starttag(self, tag, attrs):
        # breakpoint()
        tag_inst = HTMLTag(tag, attrs, self.last_parent)
        if tag == 'html':
            self.root = tag_inst
        if tag not in flat_tags:
            self.last_parent = tag_inst
        self.last_tag = tag_inst
    
    def handle_endtag(self, tag):
        # breakpoint()
        if tag not in flat_tags:
            self.last_parent = self.last_parent.parent
    
    def handle_data(self, data):
        # breakpoint()
        self.last_tag.data += data.strip()


parser = Documentation()
parser.feed(html_doc)


edited_file.write_text(str(parser.root), encoding='utf-8')

text = ''
for tag in parser.root[1].iter_all():
    if tag.name == 'section' and tag.attrs['id'] == 'module-html.parser':
        for tag_q in tag.iter_all():
            text += tag_q.data

