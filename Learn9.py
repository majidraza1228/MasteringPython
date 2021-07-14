import requests
from requests.auth import HTTPBasicAuth

# github username
username = "majidraza1228"
# url to request
url = f"https://api.github.com/users/{username}"
# make the request and return the json
#response = requests.get("http://api.open-notify.org/astros.json")
# Making a get request
"""
response = requests.get(url)
print(f"First Reponse {response}")
"""
response=  requests.get("https://api.github.com/users",  headers={'Accept': 'application/json'},auth = HTTPBasicAuth("", "")) 

# print request object
#print(f"Second Respone {response}")

for i in range(1, 11):  # A sequence from 1 to 10
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")