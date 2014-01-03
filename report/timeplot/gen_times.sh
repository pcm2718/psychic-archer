#!/bin/bash

mkdir -p timedat

for i in {7..14}
do
	for j in {0..9}
	do
		NODES=$(sed -n 7,231p ../../tsp_graphs/tsp225.txt | shuf -n $i)
		for search in a b c d
		do
			echo -n "$NODES" | python ../../src/test.py $search "inf" | cut -d'!' -f3 >> timedat/timedat_${search}_${i}.dat &
		done
	done
done
