#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:59:34 2026

@author: megancicerello
"""

from ehr_visit import EHRVisit
from datetime import datetime

INPUT_FILE = "ehr_mock_data.csv"

# ---------------------
# TRANSFORM FUNCTIONS
# ---------------------

def calculate_age(dob):
    dob_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - dob_date.year
    if (today.month, today.day) < (dob_date.month, dob_date.day):
        age -= 1
    return age


def normalize_text(value):
    return value.strip().title()


# ---------------------
# EXTRACT & LOAD
# ---------------------

def extract_and_transform(filename):
    visits = []
    diagnoses = set()

    try:
        with open(filename, "r") as file:
            header = file.readline()  # Skip header row

            for line in file:
                fields = line.strip().split(",")

                if len(fields) != 12:
                    continue

                try:
                    patient_id = int(fields[0])
                    first_name = normalize_text(fields[1])
                    last_name = normalize_text(fields[2])
                    dob = fields[3]
                    age = calculate_age(dob)
                    icd10 = fields[4].upper()
                    diagnosis = normalize_text(fields[5])
                    facility = normalize_text(fields[6])
                    risk_level = normalize_text(fields[7])
                    specialty = normalize_text(fields[8])
                    admission_date = fields[9]
                    los = int(fields[10])
                    cost = float(fields[11])
                except ValueError:
                    continue

                visit = EHRVisit(
                    patient_id,
                    first_name,
                    last_name,
                    dob,
                    age,
                    icd10,
                    diagnosis,
                    facility,
                    risk_level,
                    specialty,
                    admission_date,
                    los,
                    cost
                )

                visits.append(visit)
                diagnoses.add(icd10)

    except FileNotFoundError:
        print("EHR data file not found.")

    else:
        print("EHR data successfully extracted and transformed.")

    return visits, diagnoses


# ---------------------
# REPORTING (LOAD USE)
# ---------------------

def generate_report(visits):
    summary = {}

    for visit in visits:
        key = visit.icd10_code

        if key not in summary:
            summary[key] = {
                "diagnosis": visit.diagnosis_name,
                "count": 0,
                "total_cost": 0,
                "specialties": set()
            }

        summary[key]["count"] += 1
        summary[key]["total_cost"] += visit.get_cost()
        summary[key]["specialties"].add(visit.specialty)

    return summary


def print_report(summary):
    print("\nCLINICAL SUMMARY REPORT")
    print("-----------------------")

    for code, data in summary.items():
        avg_cost = data["total_cost"] / data["count"]

        report_tuple = (
            code,
            data["diagnosis"],
            data["count"],
            round(avg_cost, 2)
        )

        print(f"\nICD-10: {report_tuple[0]}")
        print(f"Diagnosis: {report_tuple[1]}")
        print(f"Number of Visits: {report_tuple[2]}")
        print(f"Average Cost: ${report_tuple[3]}")


# ---------------------
# MAIN EXECUTION
# ---------------------

def main():
    visits, diagnoses = extract_and_transform(INPUT_FILE)

    if not visits:
        print("No valid EHR records found.")
        return

    print(f"Unique ICD-10 Codes: {len(diagnoses)}")

    summary = generate_report(visits)
    print_report(summary)


if __name__ == "__main__":
    main()