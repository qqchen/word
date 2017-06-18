# -*- coding: utf-8 -*-
import time
import sys
import glob
import uniout
from cprint import cprint

reload(sys)
sys.setdefaultencoding('utf-8')

type = sys.getfilesystemencoding()

def parse_file(file):
	file_object = open(file, 'r')
	lines = file_object.readlines()
	file_object.close()
	return lines
	#for l in lines:
		#print l.decode('string_escape')
	#	print l.decode('UTF-8').encode(type)

def parse_word(line):
	data = line.split(' ')
	return data

def get_txt_files(dir):
	str = dir + '*.txt'
	return glob.glob(str)
'''
data_dir = 'data/'

files = get_txt_files(data_dir)

for f in files:
	parse_file(f)

'''