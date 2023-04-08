import requests

url = 'https://api.github.com/users/avielb/repos'

count = 0
response = requests.get(url.format())

if response.status_code == 200:
    repositories = response.json()
    for repository in repositories:
        count += 1
    if count >= 5:
        print("Test succeed, more than 5 repos")
else:
    print("Failed")

