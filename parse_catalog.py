from pecha_preparation_components.catalog_parser import cat_parser

cat_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTMygNIcWMvE-ifnrh5fdV3E789NiKPrLn-jdAmSuH70h1nWDjerDw77hxUd6QbVw/pub?output=xlsx'
out_path = 'input_for_op_toolkit/catalog'

cat_parser(cat_link, out_path)
