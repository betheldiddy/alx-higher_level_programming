#!/usr/bin/python3
"""
Accepts URL, sends request to the URL and shows the value of the
X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
