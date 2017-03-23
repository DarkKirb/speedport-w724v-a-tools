#!/usr/bin/env python3
import main
connect=main.getConfig("connect.json")
print("Your IPv4 Address:",connect["public_ip_v4"])
print("Your IPv6 Address:",connect["public_ip_v6"])
