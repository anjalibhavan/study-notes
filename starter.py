import sys
from datetime import datetime
import os
from pathlib import Path

now = datetime.now()
finaldate = now.strftime('%d-%m-%Y')
subject_name = sys.argv[1]
chapter_name = sys.argv[2]
cur_path = Path().absolute()
dirpath = os.path.join(cur_path, subject_name)

if not os.path.exists(cur_path):
    print('This directory does not exist.', cur_path)
    sys.exit()

if not os.path.exists(dirpath):
    os.makedirs(dirpath)

subjectpath = os.path.join(dirpath, str(chapter_name))

if not os.path.exists(subjectpath):
    os.makedirs(subjectpath)

filepath = os.path.join(subjectpath, str(chapter_name)+'.tex')

lines = [r'\documentclass{article}', r'\input{../preamble.tex}', 
            r'\title{}', r'\date{%s}' % finaldate, 
            r'\author{Anjali Bhavan}', r'\begin{document}', 
            r'\maketitle', r'\end{document}']

with open(filepath, 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')