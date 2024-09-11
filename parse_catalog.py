from src.catalog_parser import parser

cat_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTMygNIcWMvE-ifnrh5fdV3E789NiKPrLn-jdAmSuH70h1nWDjerDw77hxUd6QbVw/pub?output=xlsx'
out_path = 'input texts/catalog'

parser(cat_link, out_path)