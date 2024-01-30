import sys
import json  # Import the json module for handling JSON files
import requests
from functions import readEndpoints, readCliArguments

# Parse console arguments
args = readCliArguments()
if args.verbose:
    print("Running scan on: " + args.Url)

proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

# Load headers from a JSON file if provided, otherwise use hardcoded headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "application/json; charset=utf-8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
}

if args.headersfile:
    try:
        with open(args.headersfile, 'r') as json_file:
            custom_headers = json.load(json_file)
        headers.update(custom_headers)
    except FileNotFoundError:
        print(f"Error: Headers file '{args.headersfile}' not found. Using hardcoded headers.")


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

# Read endpoints from file
endpoints = readEndpoints("endpoints.txt")
if not endpoints:
    sys.exit()

# Access all endpoints with all HTTP verbs
for e in endpoints:
    url = args.Url + e

    for v in verbs:
        if args.verbose:
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
