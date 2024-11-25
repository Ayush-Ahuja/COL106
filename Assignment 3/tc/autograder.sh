#!/bin/bash

index=0

for folder in ../submissions/*; do
    python autograder.py "$index"
    echo "Autograded $index"
    ((index++))
done

python autograder.py -1