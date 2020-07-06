#!/usr/bin/python3

# This program takes ngram data as input, and provides a filtered version as output.
# It discards the year data, and sums the match count for each word.
# This filter can be run while downloading using curl, to reduce the size of the saved data.

import sys

# minimum number of times word should appear
MIN = 100

# minimum year for inclusion
MINYEAR = 1950

# initial values
word = ''
match_count = 0

# read from stdin until end of file
line = sys.stdin.readline()
while line != "":
	splitline = line.rstrip().split("\t")
	# only interested in years starting with MINYEAR
	if(int(splitline[1]) >= MINYEAR):	
		# if new word
		if(splitline[0] != word):						
			# if we should output word
			if(word != '' and match_count >= MIN):		
				# output word data
				print(word,"\t",match_count)			
			# set values for new word
			word = splitline[0]
			match_count = int(splitline[2])
		else:
			# existing word
			match_count = match_count + int(splitline[2])
	line = sys.stdin.readline()

# output last word data
if(match_count >= MIN):
	print(word,"\t",match_count)

# done