#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve_20():
    """jsonを返す

    """
    import gzip
    import json
    path = 'data/jawiki-country.json.gz'
    with gzip.GzipFile(path) as fin:
        for line in fin:
            line = line.decode('utf8').strip()
            article = json.loads(line)
            if article['title'] == 'イギリス':
                return article['text']

def solve_21():
    text = solve_20()
    ans = []
    for line in text.splitlines():
        if line.startswith('[[Category:'):
            ans.append(line)

    return '\n'.join(ans)


def solve_22():
    text = solve_20()
    ans = []
    for line in text.splitlines():
        if line.startswith('[[Category:'):
            cat = line.split(':')[1].split('|')[0]
            ans.append(cat)

    return '\n'.join(ans)


def solve_23():
    text = solve_20()
    ans = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('=') and line.endswith('='):
            n = len(line)
            line = line.strip('=')
            level = (n - len(line)) // 2 - 1
            ans.append('{} {}'.format(n, level))

    return '\n'.join(ans)


def solve_24():
    import re
    text = solve_20()
    ans = []
    matcher = re.compile(r'ファイル:([^|\]]+\.[a-zA-Z0-9]+)')
    for line in text.splitlines():
        for m in matcher.finditer(line):
            ans.append(m.group(1))

    return '\n'.join(ans)


def scan_basicinfo(text):
    isin = False
    for line in text.splitlines():
        if line.startswith('{{基礎情報 '):
            isin = True
        elif isin and line.startswith('|'):
            yield line.lstrip('|').split(' = ')
        elif isin and line.endswith('}}'):
            isin = False

def solve_25():
    text = solve_20()
    return {title: content for title, content in scan_basicinfo(text)}


def solve_26():
    text = solve_20()

    def strip_emphasize(string):
        import re
        return re.sub(r"('+)(.+)\1", r'\2', string)

    return {
        title: strip_emphasize(content)
        for title, content in scan_basicinfo(text)
    }


def solve_27():
    def convert_internal_link(string):
        import re
        return re.sub(
            r"\[\[([^|#\]]+)((#[^|#\]]+)?\|[^|\]]{1,})?\]\]", r'\1', string)

    return {
        title: convert_internal_link(content)
        for title, content in solve_26().items()
    }


def solve_28():
    import re
    ptn_rep = [
        (r"<([a-zA-Z]+)( [^>]+)?>([^<]+)</\1>|<[^>]+\s*/\s*>", r'\2'),
        (r"{{[^}]+}}", r''),
        (r"<ref>", r''),
        (r'\[\[ファイル:.+\]\]', ''),
    ]

    def remove_tags(string):
        # return string
        for ptn, rep in ptn_rep:
            string = re.sub(ptn, r'', string)
        return string

    return {
        title: remove_tags(content)
        for title, content in solve_27().items()
    }


def solve_29():
    endpoint = 'https://ja.wikipedia.org/wiki'
    nation_flag = solve_28()['国旗画像']
    nation_flag = nation_flag.replace(' ', '_')
    return '{endpoint}/ファイル名:{nation_flag}'.format(**locals())


if __name__ == '__main__':
    from pprint import pprint
    # pprint(solve_26())
    pprint(solve_29())
