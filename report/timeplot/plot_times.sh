#!/bin/bash

mkdir -p tmp
rm tmp/*

# Generate data files.
for search in a b c d
do
	for i in {7..14}
	do
		while read line
		do
			name=$line
			echo "$i $name" >> tmp/times_search_${search}.dat
		done < timedat/timedat_${search}_${i}.dat
	done
done

# Averages.
for search in a b c d
do
	for n in {7..14}
	do
		echo "$n `grep "$n " tmp/times_search_${search}.dat | python avg.py`" >> tmp/avg_search_${search}.dat
	done
done

# Actually do the plotting.
gnuplot plot.plot
