i=10
budget=inf

for j in {0..0}
do
	NODES=$(sed -n 7,231p tsp_graphs/tsp225.txt | shuf -n $i)
	for search in d
	do
		time (echo "$NODES" | python src/test.py $search $budget)
		echo ""
	done
	echo ""
done
