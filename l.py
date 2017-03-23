import requests
import hashlib
hp=requests.get("http://192.168.2.1/html/login/index.html")
lines=hp.text.split('\r\n')
csrf=lines[11][22:-2]
challenge=lines[12][21:-2]
print(csrf)
print(challenge)
x=hashlib.sha256(challenge.encode("UTF-8") + b":hunter2").hexdigest()
print(x)
r=requests.post("http://192.168.2.1/data/Login.json", data = {"csrf_token":csrf, "password":x, "showpw":"0", "challengev":challenge})
print(r.text)
