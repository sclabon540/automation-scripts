# Automated Data Backup Script(Python)

## Overview
This Python script automates the process of reading a file, creating a backup, validating the backup, and logging all steps. It is designed to ensure reliable workflows, reduce manual errors, and provide clear error reporting.

---

## Features
Reads an input file ('data.txt') and creates a backup ('backup.txt')
Validates that backup file was created successfully
Logs each step with timestamps in 'automation.log'
Handles errors gracefully and reports them in the console and log file,
Clear print statements and detailed logging

## Technologies used
Python 3.14
'os' module (file handling)
'logging' module(process logging)

## How to run
Make sure Python 3.14 is installed.
Place your input file 'data.txt' in the same folder as the script.
Open terminal in the project folder.
Run the script:

''' bash
python automation_script.py
