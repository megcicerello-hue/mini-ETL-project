# mini-ETL-project
Mini ETL Pipeline for Simulated EHR Visit Data

Project Overview
This project implements a mini Extract, Transform, Load (ETL) pipeline using Python to process simulated Electronic Health Record (EHR) visit data. The application reads structured healthcare data from a CSV file, cleans and standardizes the data, and generates a clinical summary report.
The project demonstrates core Python programming concepts such as file input/output, data validation, object-oriented programming, and unit testing, all applied to a realistic healthcare data scenario.

All data used in this project is synthetic and intended strictly for educational purposes.

What the Program Does
* Extracts EHR-style visit data from a CSV file
* Validates and cleans individual records
* Normalizes diagnosis codes and text fields
* Calculates patient age from date of birth
* Stores cleaned records as Python objects
* Aggregates visits by ICD-10 diagnosis
* Outputs a clinical summary report including visit counts and average cost

Why the Program Is Useful
Healthcare data is often inconsistent and requires cleaning before it can be analyzed. This project demonstrates how Python can be used to transform raw EHR-style data into meaningful summaries using simple, readable code.

The project is useful as an educational example of:
* Realistic healthcare data workflows
* Applying Python to data cleaning and transformation
* Producing reports that support healthcare analytics

Project Structure
mini_ETL_project/
|
|-- main.py			# Main ETL pipeline controller
|-- ehr_visit.py		# EHRVisit class definition
|-- ehr_mock_data.csv		# Input dataset (simulated EHR data)
|-- test_ehr_visit.py  	 	# Unit tests using assert statements
|-- README.txt     		# Project summary & instruction

Input Data Description
The program uses a CSV (comma-separated values) file containing 1,000 simulated patient visit records. Each row represents a single healthcare encounter and includes demographic, clinical, and cost-related information.

Data Dictionary
Column Name	Description			Data Type	Example
patient_id	Unique patient identifier	Integer		100123
first_name	Patient first name		String		John
last_name	Patient last name		String		Doe
date_of_birth	Patient date of birth		Date (YYYYMMDD)	19780512
icd10_code	ICD10 diagnosis code		String		J10
diagnosis_name	Diagnosis description		String		Influenza
facility	Healthcare facility name	String		City Hospital
risk_level	Clinical risk category		String		Medium
specialty	Medical specialty		String		Cardiac
admission_date	Admission date			Date (YYYYMMDD)	20240602
length_of_stay	Length of stay in days		Integer		5
cost		Total visit cost (USD)		Float		3400.75

Derived values such as patient age and summary statistics are calculated during program execution.

How to Run the Program
Requirements
* Python 3.x
* No third party libraries required

Steps
1. Place all project files in the same directory
2. Open a terminal or Spyder IDE
3. Set the working directory to the project folder
4. Run the program: python main.py/
The clinical summary report will be displayed in the console.

How to Run Unit Tests
* The file test_ehr_visit.py contains unit tests that validate public methods of the EHRVisit class.
* To run the tests: python test_ehr_visit.py
* If no output appears, all tests passed successfully.

Python Concepts Demonstrated
* Lists, sets, tuples, and dictionaries
* Conditional statements (if)
* Iteration (for loops)
* File input/output
* Error handling using try / except / else
* Userdefined functions
* Objectoriented programming
* Public and private attributes and methods
* Magic methods
* Unit testing with assertions
* Docstrings for files, functions, classes, and methods

ThirdParty Dependencies
None. This project uses only Python’s builtin libraries.

Educational Purpose
This project is intended for educational use only. It does not use real patient data and does not represent a production healthcare system.
