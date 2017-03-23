#!/usr/bin/env python3
import uptime
import tabulate

lan=uptime.lan
table=[]
for row in lan["addmdevice"]:
    table.append([row["mdevice_name"], row["mdevice_mac"], row["mdevice_ipv4"], row["mdevice_ipv6"], row["mdevice_connected"]])
print(tabulate.tabulate(table, headers=["Name", "MAC", "IP", "IPv6", "Connected"]))
