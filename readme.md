# Asset Validator
Validate API credentials and route traffice through intercepting proxy on `127.0.0.1:8080`.

## Usage

Update `baseurl` with the root of an API and `endpoints` with a list of endpoints as follows:

```python
baseurl = "https://example"
endpoints = ['/api/v0/s3/example','/api/v0/storage','/api/v0/oauth/token','/api/v0/oauth/introspect','/api/v0/s3/example/test-dir']
```

To run the program:

```bash
python3 proxy.py
```