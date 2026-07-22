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

## How to Run This Project (Beginner Guide)

### 1. Clone the Repository

Download the project from GitHub using:

```bash
git clone https://github.com/Abigail-Cobbina/lab1_Abigail-Cobbina.git
```

Navigate into the project folder:

```bash
cd lab1_Abigail-Cobbina
```

---

### 2. Run the Grade Evaluator Python Program

First, check that Python 3 is installed:

```bash
python3 --version
```

Run the Python program:

```bash
python3 grade-evaluator.py
```

When the program asks for the CSV file name, enter:

```bash
grades.csv
```

The program will:
- Read the assignment data from the CSV file
- Validate scores and assignment weights
- Calculate the total weighted grade
- Calculate the GPA
- Display the student's pass/fail status
- Display formative assignments eligible for resubmission (if applicable)

---

### 3. Run the Organizer Shell Script

Before running the shell script, give it permission to execute:

```bash
chmod +x organizer.sh
```

Run the script:

```bash
./organizer.sh
```

The script will:
- Create an `archive` directory if it does not exist
- Rename and move the current `grades.csv` file into the archive folder using a timestamp
- Create a new empty `grades.csv` file for future grade records
- Save the archive details in `organizer.log`

---

### 4. Project Files

| File | Purpose |
|---|---|
| `grade-evaluator.py` | Python program that processes grades, calculates GPA, and determines pass/fail status |
| `organizer.sh` | Bash script that archives grade files and creates logs |
| `grades.csv` | CSV file containing assignment records used by the Python program |
| `README.md` | Documentation and instructions for using the project |

---
