#!/usr/bin/env python3
"""Verifica a integridade das páginas antes de publicar.

Sem dependências — só a biblioteca padrão. Falha (exit 1) se:
  - alguma referência interna (href/src em HTML, url() em CSS) apontar para um
    arquivo que não existe no repositório;
  - alguma <img> não tiver o atributo alt (alt="" é permitido: decorativa).

Referências externas (http, //, mailto:, tel:, data:) e âncoras (#) são
ignoradas — este check cuida do que quebraria a página servida da própria
origem, não de links externos.
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.getcwd()  # o checkout do Actions deixa o cwd na raiz do repositório
errors = []


def is_external(url):
    return bool(re.match(r'^(https?:)?//|^(mailto:|tel:|data:|#)', url))


def resolve(ref, base_dir):
    """Caminho absoluto de uma referência interna, ou None se for só âncora/query."""
    ref = ref.split('#')[0].split('?')[0]
    if not ref:
        return None
    if ref.startswith('/'):          # absoluta ao site → raiz do repo
        ref = ref.lstrip('/')
        base_dir = ROOT
    if not ref:
        return None
    return os.path.normpath(os.path.join(base_dir, ref))


class PageParser(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.refs = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for key in ('href', 'src'):
            if d.get(key):
                self.refs.append(d[key])
        if tag == 'img' and 'alt' not in d:
            errors.append(f"{self.page}: <img> sem atributo alt (src={d.get('src', '?')})")


def check_html():
    for name in sorted(f for f in os.listdir(ROOT) if f.endswith('.html')):
        path = os.path.join(ROOT, name)
        with open(path, encoding='utf-8') as fh:
            parser = PageParser(name)
            parser.feed(fh.read())
        for ref in parser.refs:
            if is_external(ref):
                continue
            target = resolve(ref, ROOT)
            if target and not os.path.exists(target):
                errors.append(f"{name}: referência quebrada → {ref}")


def check_css():
    css = os.path.join(ROOT, 'assets', 'css', 'site.css')
    if not os.path.exists(css):
        return
    with open(css, encoding='utf-8') as fh:
        content = fh.read()
    for match in re.finditer(r'url\(\s*["\']?([^"\')]+)["\']?\s*\)', content):
        ref = match.group(1)
        if is_external(ref):
            continue
        target = resolve(ref, os.path.dirname(css))
        if target and not os.path.exists(target):
            errors.append(f"assets/css/site.css: referência quebrada → {ref}")


def main():
    check_html()
    check_css()
    if errors:
        print("Verificação falhou:\n")
        for e in errors:
            print(f"  - {e}")
        print(f"\n{len(errors)} problema(s). Corrija antes de publicar.")
        sys.exit(1)
    print("OK — referências internas e atributos alt conferidos.")


if __name__ == "__main__":
    main()
