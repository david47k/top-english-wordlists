#!/usr/bin/python3

# This program takes processed ngram data as input, and provides just the words as output.

import sys

# read from stdin until end of file
line = sys.stdin.readline()
while line != "":
	splitline = line.split("\t")
	print(splitline[0].rstrip())
	line = sys.stdin.readline()

# done