import sys
import requests

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

baseurl = "https://catfact.ninja/"

# Read endpoints from file
endpoints = []
try:
    fh = open("entrypoints.txt132123123", "r")
    for line in fh.readlines():
        endpoints.append(line.rstrip())
    fh.close()
except FileNotFoundError as error:
    print(error)
    exit()

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
