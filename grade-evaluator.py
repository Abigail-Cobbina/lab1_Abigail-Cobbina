import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
   
    if len(data) == 0:
        print("Error: CSV file is empty.")
        sys.exit(1)

    # TODO: a) Check if all scores are percentage based (0-100)
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    # TODO: c) Calculate the Final Grade and GPA
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
    for assignment in data:
        if assignment['score'] < 0 or assignment['score'] > 100:
            print("Error: Score must be between 0 and 100.")
            sys.exit(1)
    
    total_weight = 0
    formative_weight = 0
    summative_weight = 0

    for assignment in data:
        total_weight += assignment['weight']

        if assignment['group'] == "Formative":
            formative_weight += assignment['weight']

        elif assignment['group'] == "Summative":
            summative_weight += assignment['weight']


    if total_weight != 100:
        print("Error: Total weight must equal 100.")
        sys.exit(1)

    if formative_weight != 60:
        print("Error: Formative weight must equal 60.")
        sys.exit(1)

    if summative_weight != 40:
        print("Error: Summative weight must equal 40.")
        sys.exit(1)
    
    total_grade = 0
    formative_grade = 0
    summative_grade = 0

    for assignment in data:
        weighted_score = (assignment['score'] * assignment['weight']) / 100

        total_grade += weighted_score

        if assignment['group'] == "Formative":
            formative_grade += weighted_score

        elif assignment['group'] == "Summative":
            summative_grade += weighted_score

    gpa = (total_grade / 100) * 5.0

    if formative_grade >= 30 and summative_grade >= 20:
        status = "PASSED"
    else:
        status = "FAILED"

    
    print(f"Total Grade: {total_grade}%")
    print(f"GPA: {gpa}")
    print(f"Status: {status}")

    failed_formative = []

    for assignment in data:
        if assignment['group'] == "Formative" and assignment['score'] < 50:
            failed_formative.append(assignment)

    highest_weight = 0

    for assignment in failed_formative:
        if assignment['weight'] > highest_weight:
            highest_weight = assignment['weight']

    resubmission = []

    for assignment in failed_formative:
        if assignment['weight'] == highest_weight:
            resubmission.append(assignment)

    if resubmission:
        print("Eligible for resubmission:")

        for assignment in resubmission:
            print(f"- {assignment['assignment']}")
    else:
        print("No resubmission required.")        

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
