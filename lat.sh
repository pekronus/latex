#!/bin/bash
set -x
filetex=$1.tex
echo $filetex
python generate_exam4.py $filetex $2
latex $filetex
dvipdf $1
evince $1.pdf

