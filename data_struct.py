# -*- coding: utf-8 -*-
import sys
from parse_func import *

def print_chi(chi_str):
	encode_type = sys.getfilesystemencoding()
	print chi_str.decode('UTF-8').encode(encode_type)

class Word(object):

	def __init__(self, eng, chi):
		self.eng = eng
		self.chi = chi

	def get_eng(self):
		return self.eng

	def get_chi(self):
		return self.chi

	def print_eng(self):
		print self.eng

	def print_chi(self):
		print_chi(self.chi)

	def print_word(self):
		encode_type = sys.getfilesystemencoding()
		str = self.eng + ' ' + self.chi.decode('UTF-8').encode(encode_type)
		print str

#w = Word('english', u'英语')
#print w.get_eng(), w.get_chi()

class WordList(object):

	words = []

	def parse_words(self, file):
		lines = parse_file(file)
		for l in lines:
			data = parse_word(l)
			#print_chi(data[1])
			self.words.append(Word(data[0], data[1]))
	def __init__(self, file):
		self.file = file

	def word_num(self):
		return len(self.words)

	def print_words(self):
		for w in self.words:
			w.print_word()


'''
file = 'data/2017-06-18.txt'
wl = WordList(file)
wl.parse_words(file)
print wl.word_num()
print wl.print_words()
'''
