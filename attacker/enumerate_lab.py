import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
import requests

def make_run_folder(domain: str) -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    folder = Path("reports/") / f"{domain}-{ts}"
    folder.mkdir(parents = True, exist_ok = False)
    return folder

def fetch_url (url:str, outfile: Path):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        outfile.write_text(r.text, encoding="utf-8")
        return True
    except Exception as e:
        outfile.write_text(f"ERROR: {e}", encoding="utf-8")
        return False

def fetch_headers(domain:str, outfile: Path):
    try:
        r = requests.head(f"https://{domain}/", timeout = 10, allow_redirects=True)
        lines = [f"{k}: {v}" for k,v in r.headers.items()]
        outfile.write_text("\n".join(lines),encoding="utf-8")
    except  Exception as e:
        outfile.write_text(f"ERROR: {e}", encoding="utf-8")

def fetch_cert(domain:str, outfile: Path):
    try:
        cmd = ["openssl", "s_client", "-connect", f"{domain}:443", "-showcerts"]
        raw = subprocess.run(cmd, input=b"",capture_output=True,timeout=10)
        outfile.write_bytes(raw.stdout)
    except Exception as e:
        outfile.write_text(f"ERROR: {e}", encoding="utf-8")

def fetch_whois(domain:str, outfile: Path):
    try:
        raw = subprocess.run(["whois", domain], capture_output=True, text=True,timeout=10)
        outfile.write_text(raw.stdout, encoding="utf-8")
    except Exception as e:
        outfile.write_text(f"ERROR: {e}", encoding="utf-8")

def write_notes(folder: Path, domain: str):
    ts = datetime.now(timezone.utc).isoformat()
    notes = f"""OSINT-LAB SNAPSHOT
    Domain: {domain}
    When: {ts}
    Tools: requests, openssl, whois
    """
    (folder/"notes.txt").write_text(notes,encoding="utf-8")


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python attacker/enumerate_lab.py <domain>")
        sys.exit(1)
    domain = sys.argv[1]
    folder = make_run_folder(domain)

    # Fetch artifacts
    fetch_url(f"https://{domain}/robots.txt", folder/"robots.txt")
    fetch_url(f"https://{domain}/sitemap.xml", folder/"sitemap.xml")
    fetch_url(f"https://{domain}/", folder/"homepage.html")
    fetch_headers(domain, folder/"headers.txt")
    fetch_cert(domain, folder/"cert_info.txt")
    fetch_whois(domain, folder/"whois.txt")
    write_notes(folder, domain)

    print(f"Snapshot complete: {folder}")

if __name__ == "__main__":
    main()