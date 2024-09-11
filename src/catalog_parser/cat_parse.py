import tempfile
import urllib3
import json
from pathlib import Path

from .catalog_manager import CatalogManager


def parser(cat_link, out_path):
    # B.1 download the catalog
    http = urllib3.PoolManager()
    r = http.request('GET', cat_link, preload_content=False)
    tmp = tempfile.NamedTemporaryFile(mode='wb', suffix='.xlsx')
    while True:
        data = r.read(65536)
        if not data:
            break
        tmp.write(data)
    r.release_conn()

    # B.2 parse the catalog
    cm = CatalogManager(tmp.name, out_path)
    catalog = cm.parse_catalog()
    cat_json = json.dumps(catalog, ensure_ascii=False, indent=4)
    out_file = Path(out_path) / 'catalog.json'
    out_file.write_text(cat_json, encoding='utf-8')
