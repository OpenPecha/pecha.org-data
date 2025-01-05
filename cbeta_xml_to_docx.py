from pathlib import Path
import re

from pecha_preparation_components import parse_cbeta_xml_triplets


in_folder = Path('input/input_raw/kumarajiva/Gold Standard')
out_folder = Path('output')
parse_cbeta_xml_triplets(in_folder, out_folder)
