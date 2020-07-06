#!/usr/bin/python3

# This program takes processed ngram data as input, and provides a filtered version as output.
# It restricts the words extracted to those that end in the type specified
# e.g. NOUN will extract only nouns
# It also strips the type from the word
# Provide no type and it will only list untyped words
# The second parameter may be set to 'lower' to make all output lowercase

# e.g. ./filter2.py none lower

import sys

# defaults
filter = 'NONE'
case = 'MIXED'

# get command line parameter
if len(sys.argv) >= 2:
	filter = sys.argv[1].upper()
if len(sys.argv) >= 3:
	case = sys.argv[2].upper()
	
# read from stdin until end of file
line = sys.stdin.readline()
while line != "":
	splitline = line.rstrip().split("\t")
	# if word has a type appended
	if('_' in splitline[0]):
		# extract the word and type
		rp = splitline[0].rpartition('_')
		word = rp[0]
		type = rp[2].rstrip()
		# output the word if it has the specified type
		if(filter == type):
			if(case == 'LOWER'): word = word.lower()
			print(word,"\t",splitline[1])
	elif(filter=='NONE'):
		# output the word if it has no type
		if(case == 'LOWER'): splitline[0] = splitline[0].lower()
		print(splitline[0],"\t",splitline[1])
	line = sys.stdin.readline()

# done