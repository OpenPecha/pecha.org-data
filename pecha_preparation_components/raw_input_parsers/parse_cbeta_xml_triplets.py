import re
from pathlib import Path
from collections import defaultdict
from docx import Document  # from bayoo_docx


def parse_triplets(in_folder):
    # requires xml files triplets each in a sub_folder.  no more than 1 level
    total = {}
    for folder in Path(in_folder).glob("*"):
        files = list(folder.glob("*.xml"))
        tri = defaultdict(dict)
        for f in files:
            stem = f.stem
            stem = stem if '.' not in stem else stem.split('.')[0]
            if '.bo.zh' in f.name or '.bo.cn' in f.name or '.Tib.Chn' in f.name or '.BO.CN' in f.name:
                tri[stem]['bo_zh'] = f
            elif '.zh' in f.name or '.cn' in f.name or '.Chn' in f.name or '.CN' in f.name:
                tri[stem]['zh'] = f
            elif '.bo' in f.name or '.BO' in f.name or '.Tib' in f.name:
                tri[stem]['bo'] = f
            else:
                print('there is a problem')
                print(f)
        total[folder.name] = tri

    # check every triplet has 3 files and extract incomplete triplets
    incomplete = {}
    for folder, tri in total.items():
        keys = list(tri.keys())
        for k in keys:
            v = tri[k]
            if len(v) != 3:
                incomplete[folder] = {k: v}
                del total[folder][k]
    return total, incomplete

def parse_lang(in_file):
    dump = in_file.read_text()
    lines = dump.split('\n')
    out = {}
    for line in lines:
        if '"/>' in line:
            a = re.findall(r's id=\"([0-9\:]+)\"\/>', line)
            a.append('')
        else:
            a = re.findall(r's id=\"([0-9\:]+)\">([^<]+)<\/s>', line)
            a = a[0] if a else []
        if a:
            out[a[0]] = a[1]
    return out

def parse_table(in_file):
    dump = in_file.read_text()
    a = re.findall(r"type='([0-9\-]+)' xtargets='([0-9\:]*?)\;([0-9\:]*?)' status", dump)
    out = []
    for i, j, k in a:
        out.append({'type': i, 'zh': j, 'bo': k})
    return out

def align_triplet(triplet):
    # get file name
    name = triplet['bo'].name.split('.')[0]
    print('\t', name)

    # parse xml files
    lang1 = parse_lang(triplet['bo'])
    lang2 = parse_lang(triplet['zh'])
    table = parse_table(triplet['bo_zh'])

    # align
    aligned = []
    for t in table:
        bo, zh = t['bo'], t['zh']
        entry = ['', '']
        if bo:
            try:
                entry[0] = lang1[bo]
            except:
                print('\t\tbo: ', bo)
        if zh:
            try:
                entry[1] = lang2[zh]
            except:
                print('\t\tzh: ', zh)
        aligned.append(entry)
    return name, aligned

def write_documents(folder, filename, aligned):
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)
    doc_bo = Document()
    doc_zh = Document()
    for bo, zh in aligned:
        # add Tibetan
        doc_bo.add_paragraph(bo, style='List Number')

        # add Chinese text parsing footnotes as required
        if '^' in zh:
            par = doc_zh.add_paragraph(style='List Number')
            # extract notes from the string
            footnotes = re.findall(r'\^[0-9]+\[([^\]]+)\]', zh)
            # replace notes by * and split on * to know where to add footnotes
            parts = re.sub(r'\^[0-9]+\[[^\]]+?\]', '*', zh)
            parts = re.split(r'(\*)', parts)
            # adding text with footnotes at correct places
            f_num = 0
            for p in parts:
                if p != '*':
                    par.add_run(p)
                else:
                    try:
                        par.add_footnote(footnotes[f_num])
                        f_num += 1
                    except:
                        print(zh)
        else:
            doc_zh.add_paragraph(zh, style='List Number')
    doc_bo.save(folder / f'{filename}_bo.docx')
    doc_zh.save(folder / f'{filename}_zh.docx')

def parse_cbeta_xml_triplets(in_folder, out_folder):
    triplets, incomplete = parse_triplets(in_folder)
    for work, parts in triplets.items():
        print(work)
        out = out_folder / 'Gold Standard' / work
        for _, tri in parts.items():
            filename, aligned = align_triplet(tri)
            write_documents(out, filename, aligned)