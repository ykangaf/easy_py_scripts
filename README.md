# easy_py_scripts
Simple scripts by me

## mv_ext.py
Moves/copys/prints files with some suffix in a directory recursively to somewhere else.

Under construction. 

TODO:
Handle exceptions more carefully.


### Usage

```bash
python3 mv_ext.py [-h] [-c | -p | -m] [-o OUTPUT_DIR] i suffix

print/move/copy files recursively

positional arguments:
  i
  suffix

optional arguments:
  -h, --help            show this help message and exit
  -c, --copy
  -p, --print
  -m, --move
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR     default='.'

```
