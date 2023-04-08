import requests

url = 'http://universities.hipolabs.com/search?country=israel'

response = requests.get(url)
number_of_universities = 0
if response.status_code == 200:
    universities = response.json()
    for i in range(len(universities)):
        number_of_universities += 1
    if number_of_universities >= 5:
        print("There are more than 5 universities in Israel")
    else:
        print("Israel is lame")
