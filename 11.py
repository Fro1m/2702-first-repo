import requests

url = "https://randomuser.me/api/"

names = []
num_names = 3
count = 0
response = requests.get(f"{url}?results={num_names}")

if response.status_code == 200:
    data = response.json()
    for user in data["results"]:
        first_name = user["name"]["first"]
        response1 = requests.get(f"https://api.agify.io/?name={first_name}")
        if response1.status_code == 200:
            age = response1.json()
            if not (0 < age["age"] < 120):
                count += 1
if count == 0:
    print("Test is ok, all ages between 0-120")
else:
    print("Failed to retrieve random names")

