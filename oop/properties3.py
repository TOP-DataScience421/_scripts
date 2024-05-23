class URL:
    def __init__(self, url: str):
        url = url.rstrip('/')
        self.__url = url
        # условно-частный атриубт — ведут себя как обычно, но, по общей договорённости, игнорируются программами инспекции пространств имён не попадая в списки программ автодополнения
        self._protocol: str = ''
        self._domain: str = ''
        self._inner: str = ''
        if '//' in url:
            protocol, url = url.split('//')
            self._protocol = protocol.rstrip(':/')
            if '/' in url:
                domain, inner = url.split('/', 1)
                self._domain = domain.strip('w./')
                self._inner = inner.rstrip('./')
            else:
                self._domain = url.strip('w.')
    
    @property
    def url(self) -> str:
        return self.__url
    
    @url.setter
    def url(self, new_url: str):
        self.__dict__ |= self.__class__(new_url).__dict__
    
    # для следующих полей экземпляра определены только геттеры, следовательно их изменение (неконтроллируемое) возможно только при прямом доступе к атрибуту
    
    @property
    def protocol(self) -> str:
        return self._protocol
    
    @property
    def domain(self) -> str:
        return self._domain
    
    # для данного поля сеттер определён с выбросом специального исключения, для того чтобы не возникала проблема неопределённости с исключениями AttributeError, которые могут возникнуть по иным причинам
    
    @property
    def inner(self) -> str:
        return self._inner
    
    @inner.setter
    def inner(self, vaule):
        raise NotImplementedError


python_docs_url = URL('https://docs.python.org/3/index.html')

# доступ к атрибутам с помощью геттеров
# >>> python_docs_url.protocol
# 'https'
# >>> python_docs_url.domain
# 'docs.python.org'
# >>> python_docs_url.inner
# '3/index.html'

# прямой доступ к атрибутам остаётся без изменений
# >>> python_docs_url._protocol
# 'https'
# >>> python_docs_url._domain
# 'docs.python.org'
# >>> python_docs_url._inner
# '3/index.html'

# >>> python_docs_url.url = 'https://teams.microsoft.com/v2/'
# >>>
# >>> python_docs_url.protocol
# 'https'
# >>> python_docs_url.domain
# 'teams.microsoft.com'
# >>> python_docs_url.inner
# 'v2'

# изменение данного поля с помощью сеттера невозможно, потому что сеттер неопределён
# >>> python_docs_url.protocol = 'ftp'
# AttributeError: property 'protocol' of 'URL' object has no setter

# изменение данного поля с помощью сеттера невозможно, потому что мы явно запретили это в самом сеттере
# >>> python_docs_url.inner = '4/index.html'
# NotImplementedError

