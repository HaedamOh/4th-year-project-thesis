#!/usr/bin/python

# Author: Michael Bloesch

# Possible fields 'abstract', 'isbn', 'mendeley-groups', 'keywords', 'file', 'issn','annote','address','editor','publisher','month','url'

import os, re, sys
#import argparse
def clean(fileName, fileNameOut):
	remove_keys = ['abstract', 'isbn', 'mendeley-groups', 'keywords', 'file', 'issn','annote','address','editor','publisher','month','url','pages']
	blind_keys = ['none']
	bibf = open(fileName, 'r')
	cleanf = open(fileNameOut, 'w')
	lines = bibf.readlines()
	for line in lines:
		if re.search('^'+'|'.join(blind_keys),line):
			cleanf.write('%%%%' + line)
		elif not re.search('^'+'|'.join(remove_keys),line) and (re.search('=',line) or re.search('@',line) or line == '}\n'):
			#print line
			cleanf.write(line)
	bibf.close()
	cleanf.close()

str(sys.argv)
clean(sys.argv[1], sys.argv[2])

