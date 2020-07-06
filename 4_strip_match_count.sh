#!/bin/bash

# remove count from output files

for FILE in top_english*.txt; do
	./filter_strip_count.py < "${FILE}" > "temp"
	mv "temp" "${FILE}"
done

