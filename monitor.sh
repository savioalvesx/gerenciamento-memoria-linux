#!/bin/bash
echo "Timestamp,MemUsed,SwapUsed" > memory_usage.csv
python3 memory_overload.py & # Inicia o programa em Python em segundo plano
PYTHON_PID=$!
for i in {1..30}; do
 TIMESTAMP=$(date +"%T")
 MEM_USED=$(free -m | awk 'NR==2{print $3}')
 SWAP_USED=$(free -m | awk 'NR==3{print $3}')
 echo "$TIMESTAMP,$MEM_USED,$SWAP_USED" >> memory_usage.csv
 sleep 1
done
wait $PYTHON_PID