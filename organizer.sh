#!/bin/bash

if [ ! -d "archive" ]; then
    mkdir archive
fi

if [ ! -f "grades.csv" ]; then
    echo "Error: grades.csv not found. Nothing to archive."
    exit 1
fi

timestamp=$(date +"%Y%m%d-%H%M%S")

archived_file="grades_${timestamp}.csv"

mv grades.csv archive/$archived_file

touch grades.csv

echo "$timestamp | grades.csv | $archived_file" >> organizer.log
