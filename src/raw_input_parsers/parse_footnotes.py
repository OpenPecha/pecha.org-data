import re

def parse_cbeta_2_pecha(text: str):
    # cbeta: "^1[this is the note]"
    # pecha: "<sup class="footnote-marker">1</sup><i class="footnote">this is the note</i>"
    pattern_whole = r'(\^[0-9]+\[[^\]]+\])'
    pattern_split = r'\^([0-9]+)\[([^\]]+)\]'

    out = []
    parts = re.split(pattern_whole, text)
    for p in parts:
        if p.startswith('^') and '[' in p and p.endswith(']'):
            _, marker, text, _ = re.split(pattern_split, p)
            parsed = f'<sup class="footnote-marker">{marker}</sup><i class="footnote">{text}</i>'
            out.append(parsed)
        else:
            out.append(p)

    return ''.join(out)
