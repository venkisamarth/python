import requests
url="https://www.wscubetech.com/"
r=requests.get(url)
print(r.status_code)
print(r.text)