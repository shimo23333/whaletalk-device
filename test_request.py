import requests

url = "https://api.sampleapis.com/coffee/hot"

try:
    r = requests.get(url,timeout=3)
    r.raise_for_status()
    print(r.json())
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)     
