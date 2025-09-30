from pathlib import Path
import requests

url = "https://happyhopper.org/"                  # page to fetch
out = Path("reports/ifwoctopi.github.io-TEST/robots.txt")  # local file to write

resp = requests.get(url, timeout=10)
resp.raise_for_status()            # optional: stop on non-200
out.parent.mkdir(parents=True, exist_ok=True)  # make parent dir if needed
out.write_text(resp.text, encoding="utf-8")    # overwrite or create
print(f"Saved {len(resp.text)} bytes to {out}")
