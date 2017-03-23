#!/usr/bin/env python3
import main
import datetime
import requests
overview=main.getConfig("overview.json")
lan=main.getConfig("lan.json")
memory=eval(requests.get("http://192.168.2.1/data/memory.json", cookies=main.login.cookies).text)
count=0
for f in lan["addmdevice"]:
    if f["mdevice_connected"] == "1":
        count+=1
print(datetime.datetime.now().strftime("%H:%M:%S"), "up", overview["days_online"], "days,", overview["time_online"], ",", count, "users, load:",memory["cpu_load"])
