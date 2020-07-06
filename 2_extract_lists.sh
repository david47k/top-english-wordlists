#!/bin/bash

# produce lists from processed onegram data

PREFIX="all_english"
CASES="mixed lower"

for CASE in $CASES; do
	FILENAME="${PREFIX}_words_${CASE}.txt"
	if test -f "${FILENAME}"; then
		echo "${FILENAME} already exists, skipping."
	else
		echo "creating ${FILENAME}"
		cat onegram_*.txt | ./filter2.py none "${CASE}" | LC_ALL=C sort -f | ./filter3.py | LC_ALL=C sort -f --key=2rn > "${FILENAME}"
	fi
done


TYPES="noun verb adj adv pron det adp num conj prt"


for TYPE in $TYPES; do
	for CASE in $CASES; do
		FILENAME="${PREFIX}_${TYPE}s_${CASE}.txt"
		if test -f "${FILENAME}"; then
			echo "${FILENAME} already exists, skipping."
		else
			echo "creating ${FILENAME}"
			cat onegram_*.txt | ./filter2.py "${TYPE}" "${CASE}" | LC_ALL=C sort -f | ./filter3.py | LC_ALL=C sort -f --key=2rn > "${FILENAME}"
		fi
	done
done
