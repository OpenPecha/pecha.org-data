from ..src.raw_input_parsers import parse_cbeta_2_pecha

def test_cbeta_footnotes():
    in_strings = [
        'this is a text with ^1[note one] and ^2[note 2]',
        '^3[note 3]There is a note at the beginning!'
    ]
    expected = [
        'this is a text with <sup class="footnote-marker">1</sup><i class="footnote">note one</i> and <sup class="footnote-marker">2</sup><i class="footnote">note 2</i>',
        '<sup class="footnote-marker">3</sup><i class="footnote">note 3</i>There is a note at the beginning!'
    ]

    for n, in_str in enumerate(in_strings):
        out = parse_cbeta_2_pecha(in_str)
        assert out == expected[n]
