import argparse

def readEndpoints(filename):
    endpoints = []
    try:
        fh = open(filename, "r")
        for line in fh.readlines():
            endpoints.append(line.rstrip())
        fh.close()

        return endpoints
    except FileNotFoundError as error:
        print(error)
    return []

def readCliArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("baseurl", help="The base URL of the API")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    return parser.parse_args()
