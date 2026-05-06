import csv
import json

INPUT_FILE = r"C:\Users\ELCOT\Documents\data.csv"
CLEAN_FILE = "clean.jsonl"
ERROR_FILE = "errors.jsonl"
REPORT_FILE = "report.json"

total = 0
valid = 0
invalid = 0

with open(INPUT_FILE, "r") as csv_file, \
    open(CLEAN_FILE, "w") as clean_file, \
    open(ERROR_FILE, "w") as error_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        total += 1
        row_errors = []
        name = row.get("name")
        age = row.get("age")
        income = row.get("income")
        try:
            age = int(age)
        except:
            row_errors.append("Age is not a number")

        try:
            income = float(income)
        except:
            row_errors.append("Income is not a number")

        if isinstance(age, int) and (age < 18 or age > 60):
            row_errors.append("Age must be between 18 and 60")
        if isinstance(income, float) and income < 0:
            row_errors.append("Income cannot be negative")

        if row_errors:
            invalid += 1
            error_file.write(json.dumps({"row": row,"errors": row_errors}) + "\n")
        else:
            valid += 1
            clean_file.write(json.dumps({
            "name": name,
            "age": age,
            "income": income}) + "\n")

report = {
            "Total Rows": total,
            "Valid Rows": valid,
            "Invalid Rows": invalid,
            "Error Rate": round((invalid / total) * 100, 2)}
with open(REPORT_FILE, "w") as r:
    json.dump(report, r, indent=4)
print("Done")
