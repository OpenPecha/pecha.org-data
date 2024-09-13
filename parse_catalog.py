from catalog_parser import cat_parser

cat_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTMygNIcWMvE-ifnrh5fdV3E789NiKPrLn-jdAmSuH70h1nWDjerDw77hxUd6QbVw/pub?output=xlsx'
out_path = 'op_toolkit_input/catalog'

cat_parser(cat_link, out_path)
