#!/usr/bin/env python3
import main
import requests
import tabulate
memory=eval(requests.get("http://192.168.2.1/data/memory.json", cookies=main.login.cookies).text)
totalram=int(memory["amm"][:-3])
usedram=int(memory["used_free_main"].split(' ')[0][:-1])/100
usedram*=totalram
freeram=totalram-usedram

totalflash=int(memory["afm"][:-3])
usedflash=int(memory["used_free_lash"].split(' ')[0][:-1])/100
usedflash*=totalflash
freeflash=totalflash-usedflash

print(tabulate.tabulate([["RAM", totalram, usedram, freeram],["NAND", totalflash, usedflash, freeflash]], headers=["","total","used","free"]))
