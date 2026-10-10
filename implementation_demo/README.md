###### \# WannaCry Defensive Log Triage

###### 

###### \*\*GitHub Repository:\*\* https://github.com/anum777/wannacry-log-triage

###### 

###### \## Project Overview

###### 

###### This project demonstrates basic defensive log triage using Python and synthetic security events as part of the WannaCry ransomware case study.

###### 

###### \## Requirements

###### 

###### \- Python 3.9 or later

###### \- Dependencies listed in `requirements.txt`

###### 

###### \## How to Run

###### 

###### 1\. Open a terminal in the project directory.

###### 2\. Install dependencies if required:

###### 

###### &#x20;  `pip install -r requirements.txt`

###### 

###### 3\. Run the script:

###### 

###### &#x20;  `python triage\_logs.py synthetic\_events.csv`

###### 

###### 4\. Check the generated `triage\_alerts.csv` file.

###### 

###### \## Important Limitation

###### 

###### This is an educational demonstration using synthetic data and illustrative thresholds. It does not execute malware, access a live network, or function as a validated WannaCry detection system.

# WannaCry Case Study — Synthetic Log Triage Demo

## Purpose

A safe, small defensive demonstration for the WannaCry case study. It reads fictional event records and flags unusually frequent SMB connection events or file-change events for analyst review.

**This is not WannaCry, does not execute malware, does not exploit SMB, does not scan networks, and does not prove infection.** All data are fictional.

## Requirements

Python 3.9+; no third-party packages.

## Files

* `triage\_logs.py`: analyzes sample records and writes alerts.
* `synthetic\_events.csv`: fictional input data.
* `README.md`: these instructions.

## Run

1. Extract this ZIP.
2. Open a terminal in this folder.
3. Run `python triage\_logs.py synthetic\_events.csv`
4. Review the generated `triage\_alerts.csv`.

## Logic

A host is flagged at 20 or more SMB connection events, or 30 or more file-change events. These are illustrative thresholds, not validated real-world detection rules. Benign activity may trigger an alert; human review and correlation with other evidence are required.

## Expected behavior

The fictional `HOST-01` should be flagged for both high SMB connection count and high file-change count.

## GitHub

After creating a repository, replace this placeholder: `\[PASTE YOUR GITHUB REPOSITORY URL]`.

## Reporting note

Call this a **synthetic log triage demonstration**, not an implementation of WannaCry or a validated WannaCry detector.

