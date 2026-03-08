# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'const sentenceCatalog\s*=\s*\{([\s\S]*?)\}\s*\nconst converter', html)
if not m:
    print('catalog not found')
    exit(1)

catalog_str = m.group(0)
strings = re.findall(r'"([^"]+)"', catalog_str)
# filter: has CJK and reasonable length (sentence, not key like "日常句子")
cjk = re.compile(r'[\u4e00-\u9fff]')
sentences = [s for s in strings if cjk.search(s) and 1 <= len(s) <= 500]

all_text = ''.join(sentences)
chars = set(c for c in all_text if '\u4e00' <= c <= '\u9fff')

print('Sentences:', len(sentences))
print('Unique CJK chars:', len(chars))
with open('unique_chars.txt', 'w', encoding='utf-8') as out:
    out.write(''.join(sorted(chars)))
