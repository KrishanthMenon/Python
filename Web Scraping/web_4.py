import requests
url = "http://127.0.0.1:8000/post/"

params = {
    "offset" : "10"
}

response = requests.get(url = url , params=params)

print(response.url)