"""Educational defensive log triage demo using fictional events only.
This does not execute malware, scan networks, exploit SMB, or prove infection.
"""
import csv, sys
from collections import defaultdict

SMB_THRESHOLD = 20
FILE_CHANGE_THRESHOLD = 30

def main(path):
    totals = defaultdict(lambda: {"smb": 0, "file_change": 0})
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            host = row["source_host"].strip()
            kind = row["event_type"].strip().lower()
            count = int(row["event_count"])
            if kind == "smb_connection":
                totals[host]["smb"] += count
            elif kind == "file_change":
                totals[host]["file_change"] += count
    alerts=[]
    for host, vals in sorted(totals.items()):
        reasons=[]
        if vals["smb"] >= SMB_THRESHOLD: reasons.append("high SMB connection count")
        if vals["file_change"] >= FILE_CHANGE_THRESHOLD: reasons.append("high file-change count")
        if reasons:
            alerts.append({"source_host":host,"smb_count":vals["smb"],
                "file_change_count":vals["file_change"],"reason":"; ".join(reasons),
                "note":"synthetic heuristic; analyst review required"})
    with open("triage_alerts.csv","w",newline="",encoding="utf-8") as f:
        fields=["source_host","smb_count","file_change_count","reason","note"]
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(alerts)
    print(f"Processed {len(totals)} synthetic hosts; wrote {len(alerts)} alert(s) to triage_alerts.csv.")
    for a in alerts: print(f"- {a['source_host']}: {a['reason']}")

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Usage: python triage_logs.py synthetic_events.csv"); sys.exit(1)
    main(sys.argv[1])
