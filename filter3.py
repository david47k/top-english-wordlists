#!/usr/bin/python3

# This program takes already processed alphabetically sorted ngram data as input, and removes dupes by adding the match_count.

import sys

# initial values
word = ''
match_count = 0

# read from stdin until end of file
line = sys.stdin.readline()
while line != "":
	splitline = line.rstrip().split("\t")
	# if new word
	if(splitline[0] != word):						
		# if we should output word
		if(word != ''):		
			# output word data
			print(word,"\t",match_count)			
		# set values for new word
		word = splitline[0]
		match_count = int(splitline[1])
	else:
		# existing word
		match_count = match_count + int(splitline[1])
	line = sys.stdin.readline()

# output last word data
print(word,"\t",match_count)

# done