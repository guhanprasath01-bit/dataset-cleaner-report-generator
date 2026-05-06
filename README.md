# Dataset Cleaner & Report Generator
A simple Python project to clean, validate, and analyze CSV data.
---
## What this project does
- Reads data from a CSV file
- Validates age and income fields
- Separates valid and invalid records
- Generates a summary report
---
## Features
✔ Age validation (18–60)
✔ Income validation (> 0)
✔ Clean data stored separately
✔ Error tracking with reasons
✔ Automatic report generation
---
## Input Format
CSV file with the following structure:
name,age,income
Example:
name,age,income
Ethan,25,50000
Emma,abc,60000
---
## Output Files
| File Name | Description |
|----------------|--------------------------------|
| clean.jsonl | Valid records |
| errors.jsonl | Invalid records with errors |
| report.json | Summary of processing |
---
## How to Run
python dataset.py