# WannaCry Case Study — Synthetic Log Triage Demo

## Purpose
A safe, small defensive demonstration for the WannaCry case study. It reads fictional event records and flags unusually frequent SMB connection events or file-change events for analyst review.

**This is not WannaCry, does not execute malware, does not exploit SMB, does not scan networks, and does not prove infection.** All data are fictional.

## Requirements
Python 3.9+; no third-party packages.

## Files
- `triage_logs.py`: analyzes sample records and writes alerts.
- `synthetic_events.csv`: fictional input data.
- `README.md`: these instructions.

## Run
1. Extract this ZIP.
2. Open a terminal in this folder.
3. Run `python triage_logs.py synthetic_events.csv`
4. Review the generated `triage_alerts.csv`.

## Logic
A host is flagged at 20 or more SMB connection events, or 30 or more file-change events. These are illustrative thresholds, not validated real-world detection rules. Benign activity may trigger an alert; human review and correlation with other evidence are required.

## Expected behavior
The fictional `HOST-01` should be flagged for both high SMB connection count and high file-change count.

## GitHub
After creating a repository, replace this placeholder: `[PASTE YOUR GITHUB REPOSITORY URL]`.

## Reporting note
Call this a **synthetic log triage demonstration**, not an implementation of WannaCry or a validated WannaCry detector.
