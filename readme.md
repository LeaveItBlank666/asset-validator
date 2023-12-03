# Asset Validator
Validate API credentials and route traffic through intercepting proxy on `127.0.0.1:8080`.

## Usage

Update `baseurl` with the root of an API and `endpoints.txt` with a list of endpoints as follows:

```python
baseurl = "https://example"
```

To run the program:

```bash
python3 main.py
```

## Backlog
### 1.1.0 - Improve program
 - ~~Endpoint should be read from a file~~
 - Baseurl must be past as a CLI argument
 - Pass file with headers to be used
 - Optional: Pass custom proxy
### 1.2.0 - Validate endpoints
 - Make proxy use optional
 - Debug mode (we don't want to be reliant on a proxy)
 - Store debug output to file 1.3.0
### 1.3.0 - Validate endpoints
 - Check all endpoints with & without authorization
 - Update report
### 1.4.0 - Add OpenAPI/Swagger support
 - Support OpenApi
 - Support Swagger