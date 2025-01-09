from pathlib import Path
import re

from pecha_preparation_components import parse_cbeta_xml_triplets, recursive_copy_metadata


in_folder = Path('input/input_raw/kumarajiva/Gold Standard')
out_folder = Path('output')
parse_cbeta_xml_triplets(in_folder, out_folder)
recursive_copy_metadata(Path('input/metadata_template.xlsx'), Path('output/Gold Standard'))
