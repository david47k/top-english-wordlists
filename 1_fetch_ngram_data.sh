#!/bin/bash
BASE_URL="http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-"
ALPHABET="a b c d e f g h i j k l m n o p q r s t u v w x y z"
for CHAR in $ALPHABET; do
	if test -f "onegram_$CHAR.txt"; then
		echo "onegram_$CHAR.txt already exists, skipping."
	else
		curl http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701-$CHAR.gz | zcat | ./filter.py > onegram_$CHAR.txt
	fi
done
	