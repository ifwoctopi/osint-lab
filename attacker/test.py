import requests

resp = requests.get("https://ifwoctopi.github.io/")
print("Status:", resp.status_code)
print("First 80 chars:", resp.text[:80])