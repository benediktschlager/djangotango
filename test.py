import urllib3

no_timeout = urllib3.Timeout(total=None, connect=None, read=None)
http = urllib3.PoolManager(num_pools=999, timeout=no_timeout)

resp1 = http.request("GET", "http://localhost:8000/")
resp2 = http.request("GET", "http://localhost:8000/")
resp3 = http.request("GET", "http://localhost:8000/")
resp4 = http.request("GET", "http://localhost:8000/")
resp5 = http.request("GET", "http://localhost:8000/")
resp6 = http.request("GET", "http://localhost:8000/")
resp7 = http.request("GET", "http://localhost:8000/")

print(len(http.pools))
# 2
