# -*- coding: utf-8 -*-

"""
Install:

    cpan Unicode::Tussle

Usage:

    python unichars.py <perluniprop>

Example:

    python unichars.py \p{Currency_Symbol}

"""
from __future__ import print_function

import io
import re
import sys
import subprocess

pp = sys.argv[1]
cmd = "unichars '\\{}' | cut -f2 -d' ' | tr -d '\n'".format(pp)
charset = subprocess.check_output(cmd, shell=True).decode('utf8')
output = re.search('\{(.*?)\}', pp).group(1)
with io.open('{}.txt'.format(output), 'w', encoding='utf8') as fout:
    print(charset, file=fout)
