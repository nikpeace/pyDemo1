import request

r = requests.get("https://taskmanager.in")
print(r.status_code)
print(r.ok)
