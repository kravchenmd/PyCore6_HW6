# PyCore6: Homework 6 (Kravchenko Michail)

## Quick discription

The initial code samples were edited and written in the way to fit the requirements of the descriprion of the homework at Schoology

Main features:

- The script sorts all filed based on their types to the corresponding folder.
- Names of all files, inluding ones with uknows/not included exnextions are sanitized.
- Files with unknown/not included extention are moved to the folder with name 'OTHER_TYPES'. The name was choosen in the way to avoid the problem with existing folder 'Other' in Windows.
- `file_parser.py` contains 2 dicts: 1st one is used to determine type of file based on extention, then the 2nd one is used to choose propes container (list) for file names.
- `file_parser.py` contains some lists for tracking different folders that are used only for debugging reasons.

**_Kravchenko Michail_**
