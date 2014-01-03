#!/bin/bash

mkdir -p pathdat

NODES=$(sed -n 7,231p ../../tsp_graphs/tsp225.txt)
for budget in 14400  #1 5 10 30 60 600 1800 3600
do
	for search in a b c d
	do
		(
			ORDER=$(echo -n "$NODES" | python ../../src/test.py ${search} ${budget} | cut -d'!' -f5 | sed s/"[],[]"/""/g)
			for NODE in $ORDER
			do
				awk "{ if (\$1 == ${NODE}) print \$0 }" ../../tsp_graphs/tsp225.txt >> pathdat/pathdat_${search}_${budget}.dat
			done
		) &
	done
done
