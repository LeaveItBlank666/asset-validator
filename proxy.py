import requests

proxy = {
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080"
}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
   # "Accept": "application/json, text/plain, */*",
    "Accept": "application/json; charset=utf-8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://maritime.sealstorage.io",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ5cXRUZU1uV2k0cVRKSG85NWRPMyJ9.eyJpc3MiOiJodHRwczovL21hcml0aW1lLXNlYWxzdG9yYWdlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiIweXpGSjM0dTVjRjdSUUhWbWdWU1Z5WWN5TWswYXBtbkBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9tYXJpdGltZS5zZWFsc3RvcmFnZS5pbyIsImlhdCI6MTcwMTA5ODYwMCwiZXhwIjoxNzAxMTg1MDAwLCJhenAiOiIweXpGSjM0dTVjRjdSUUhWbWdWU1Z5WWN5TWswYXBtbiIsInNjb3BlIjoic3RvcmFnZS5uYW1lc3BhY2U6L2JyZWFjaGxvY2siLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.1rZcPI9OtjzoY1eMdWJmyo-xtwXt7YCUvVcCKRJ6XbJ-nApviQnFSke5LZKtaTbm61_WO5h_xNUhJE36Is9A1AvwYnFkMF5ElNVLcBII2oY3om8KCtrAKTPUaKYiS9dRkDpvgGcagxieDLrZ2uUyTyHb_yoOvvSjnQj4QYNYDnK1HqXpGXEta76pkAxu_ZWk38XHTgFrl2ETZ0hJHg5KDfHuR_A-LcM80SGhEpi6GWrr-g2AJdmd24GF6a46orLjX5b8vjB2xiRZbQueUwTvZ0q-p1JomJPTK6V57D8n53h6Krx3Ea6BKZVYodXxLGaYS_vFwEojcqfH47kkG227uQ"
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

baseurl = "https://maritime.sealstorage.io"
endpoints = ['/api/v0/s3/breachlock','/api/v0/storage','/api/v0/oauth/token','/api/v0/oauth/introspect','/api/v0/s3/breachlock/test-dir']

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
