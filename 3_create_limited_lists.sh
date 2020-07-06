#!/bin/bash

# produce lists from processed onegram data
# e.g. produce top_english_words_lower_1000000.txt from all_english_words_lower.txt

CASES="mixed lower"

create_files () {
	TYPES="$1"
	COUNT="$2"
	for TYPE in $TYPES; do
		for C in $COUNT; do
			for CASE in $CASES; do
				FILENAME="top_english_${TYPE}s_${CASE}_${C}.txt"
				if test -f "${FILENAME}"; then
					echo "${FILENAME} already exists, skipping."
				else
					echo "creating ${FILENAME}"
					head -n "${C}" "all_english_${TYPE}s_${CASE}.txt" > "${FILENAME}"
				fi
			done
		done
	done
}


create_files "word" "1000000"
create_files "word noun" "500000"
create_files "word noun verb adj" "10000 20000 50000 100000"
create_files "adv pron" "10000"
create_files "num conj det prt adp" "500"
