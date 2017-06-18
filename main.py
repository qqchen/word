# -*- coding: utf-8 -*-
import sys
from data_struct import *
from parse_func import *

data_dir = 'data/'

files = get_txt_files(data_dir)

print len(files)

for f in files:
	wl = WordList(f)
	wl.parse_words(f)
	print wl.word_num()
	print wl.print_words()