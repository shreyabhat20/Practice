'''You are given a raw log file which contains messages in JSON format.
Example:  {“timestamp”: “2025-10-13 20:05:05”, “level”: “ERROR”, “message”: “DB failed to connect”, “service”: “UserService”}
The log file could be very large also in GBs.
Please create a report which contains with the following
•	Count of errors per service
•	Most common error messages
•	Count of each log levels
•	Most 5 occurred logs with their count
'''
import json
from collections import Counter, defaultdict

err_per_svc=defaultdict(int)
err_msgs=Counter()
lvl_cnt=Counter()
log_cnt=Counter()

with open("test_log.jsonl","r") as f:
    for line in f:
        log=json.loads(line)
        lvl=log.get("level")
        msg=log.get("message")
        svc=log.get("service")
        lvl_cnt[lvl]+=1
        if lvl=="ERROR":
            err_per_svc[svc]+=1
            err_msgs[msg]+=1
        log_cnt[line.strip()]+=1

report={
    "Error Count per Service":dict(err_per_svc),
    "Most Common Error Messages":err_msgs.most_common(10),
    "Log Level Counts":dict(lvl_cnt),
    "Top 5 Most Frequent Logs":log_cnt.most_common(5)
}

for sec,content in report.items():
    print(f"\n{sec}:")
    if sec=="Top 5 Most Frequent Logs":
        for log_line,cnt in content:
            log=json.loads(log_line)
            print(f"{log['level']} from {log['service']}: \"{log['message']}\" (Occurred {cnt} times)")
    elif isinstance(content,dict):
        for k,v in content.items():
            print(f"{k}: {v}")
    else:
        for item,cnt in content:
            print(f"{item}: {cnt}")
