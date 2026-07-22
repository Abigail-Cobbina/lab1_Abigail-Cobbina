# Lab 1 - Grade Evaluator & Archiver

## Description

This project contains a Python application that evaluates student grades from a CSV file and a Bash script that archives course grade data.

The Python program:
- Reads assignment data from grades.csv
- Validates assignment scores and weights
- Calculates the final weighted grade
- Calculates GPA using the formula:
  
  GPA = (Total Grade / 100) * 5.0

- Determines whether the student passed or failed
- Identifies formative assignments eligible for resubmission

The Bash script:
- Creates an archive directory
- Adds a timestamp to old grade files
- Moves old grades.csv files into the archive folder
- Creates a fresh grades.csv file
- Records archive activities in organizer.log

---

## Files

### grade-evaluator.py

Python program used to process and evaluate grades.

Run using:

```bash
python3 grade-evaluator.py
```

When prompted, enter:

```bash
grades.csv
```

---

### organizer.sh

Bash script used to archive grade files.

Run using:

```bash
bash organizer.sh
```

---

### grades.csv

CSV file containing assignment information:

- Assignment name
- Assignment category (Formative/Summative)
- Score
- Weight

---

## Requirements

- Python 3
- Linux/Bash terminal

---
