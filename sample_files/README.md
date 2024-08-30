## Current limitations

`source > categories` must always be in EN even if the translation is in another language.
This is because Sefaria only supports two languages (hebrew and english).

## Conventions

1. versions and translations must have the same amount of lines as the corresponding main text.
2. if translations and versions have fewer lines, create empty lines. If they have more lines, integrate them in the preceding line. (if more lines at beginning, add them to 1st line)
3. both simple and complex texts can have versions and translations, and commentary annotations in the same file.
4. root texts are always simple texts, so they will always have `section > meaning-segment` numbers.

### Questions

- is `source > books > completestatus` field required?
- how do we represent links between texts that are not source/commentary? For ex: citation in one text linked to the text from which the citation comes from.
- how do we pass the remaining metadata, even if it won't be used for the time being?
- how do we pass long_title_clean so that it is shown in the header of the reader app?
- can we add versions and translations to commentaries just as to regular root texts?

### renaming propositions
source >> trans
target >> main
completestatus >> completionStatus
enDesc >> transDesc
enShortDesc >> transShortDesc
heDesc >> mainDesc
heShortDesc >> mainShortDesc
chapter >> section
