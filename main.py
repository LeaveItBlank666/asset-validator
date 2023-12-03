import sys
import requests
import argparse
from functions import readEndpoints

# Parse console arguments
parser = argparse.ArgumentParser()
parser.add_argument("baseurl", help="The base URL of the API")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("Running scan on: " + args.baseurl)

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "application/json; charset=utf-8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
}
verbs = [
    "HEAD",
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
    "LOCK",
    "UNLOCK"
]
baseurl = args.baseurl

# Read endpoints from file
endpoints = readEndpoints("endpoints.txt")
if not endpoints:
    sys.exit()

# Access all endpoints with all HTTP verbs
for e in endpoints:
    url = baseurl + e

    for v in verbs:
        print(f"Trying '{v}: {url}'...")

        try:
            req = requests.request(
                v,
                url=url,
                headers=headers,
                proxies=proxy,
                timeout=5,
                verify=False
            )
        except requests.exceptions.ReadTimeout:
            pass
        except:
            pass
