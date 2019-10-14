from markdown.extensions import fenced_code as org
from markdown.extensions.codehilite import CodeHilite, CodeHiliteExtension, parse_hl_lines
from .hidden_hilite import HiddenHilite
#from .codehilite import CodeHilite, CodeHiliteExtension, parse_hl_lines

import re

class FencedCodeExtension(org.FencedCodeExtension):
    def extendMarkdown(self, md):
        """ Add FencedBlockPreprocessor to the Markdown instance. """
        md.registerExtension(self)
        md.preprocessors.register(FencedBlockPreprocessor(md), 'fenced_code_block', 25)

class FencedBlockPreprocessor(org.FencedBlockPreprocessor):
    
    FENCED_BLOCK_RE = re.compile(r'''
(?P<indent>^[ \t]*)
(?P<fence>(?:~{3,}|`{3,}))[ ]*         # Opening ``` or ~~~
(\{?\.?(?P<lang>[\w#.+-]*))?[ ]*        # Optional {, and lang
# Optional highlight lines, single- or double-quote-delimited
(hl_lines=(?P<quot>"|')(?P<hl_lines>.*?)(?P=quot))?[ ]*
(:[ ]*(?P<filename>[^ ]*))?[ ]*
}?[ ]*\n                                # Optional closing }
(?P<code>.*?)(?<=\n)
[ \t]*(?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)
    def run(self, lines):
        """ Match and store Fenced Code Blocks in the HtmlStash. """

        # Check for code hilite extension
        if not self.checked_for_codehilite:
            for ext in self.md.registeredExtensions:
                if isinstance(ext, CodeHiliteExtension):
                    self.codehilite_conf = ext.config
                    
                    break

            self.checked_for_codehilite = True
        text = "\n".join(lines)
        while 1:
            m = self.FENCED_BLOCK_RE.search(text)
            if m:
                lang = ''
                if m.group('lang'):
                    lang = self.LANG_TAG % m.group('lang')
                # If config is not empty, then the codehighlite extension
                # is enabled, so we call it to highlight the code
                code = re.sub('^'+m.group('indent'), '', m.group('code'), flags=re.MULTILINE)
                filename = self.codehilite_conf.get('pygments_show_filename', '') and m.group('filename')
                if self.codehilite_conf:
                    #highliter = CodeHilite(
                    #print(self.codehilite_conf)
                    #raise KeyboardInterrupt()
                    #print(self.codehilite_conf['pygments_style'][0],)
                    #import pdb;pdb.set_trace()
                    #print(self.codehilite_conf['noclasses'])
                    #raise KeyboardInterrupt()
                    highliter = HiddenHilite(
                        src=code, 
                        linenums=self.codehilite_conf['linenums'][0],
                        guess_lang=self.codehilite_conf['guess_lang'][0],
                        css_class=self.codehilite_conf['css_class'][0],
                        style=self.codehilite_conf['pygments_style'][0],
                        use_pygments=self.codehilite_conf['use_pygments'][0],
                        lang=(m.group('lang') or None),
                        noclasses=self.codehilite_conf['noclasses'][0],
                        hl_lines=parse_hl_lines(m.group('hl_lines')),
                        filename = filename,
                    )
                    code = highliter.hilite()
                else:
                    code = self.CODE_WRAP % (lang,
                                             self._escape(m.group('code')))
                # code = code[:code.find(">")+1] + \
                #     f'<div><span class="filename">{m.group("filename") or ""}</span></div>' +\
                #     code[code.find(">")+1:]
                placeholder = self.md.htmlStash.store(code)
                placeholder = m.group('indent') + placeholder
                text = '%s\n%s\n%s' % (text[:m.start()],
                                       placeholder,
                                       text[m.end():])
            else:
                break
        return text.split("\n")

def makeExtension(**kwargs):  # pragma: no cover
    return FencedCodeExtension(**kwargs)
