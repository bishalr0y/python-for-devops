# https://api.github.com/users/username/repos
# to display project name and url

import requests

username = input("Enter your github username: ")

try:
    url = f'https://api.github.com/users/{username}/repos'
    res = requests.get(url).json()
    res = list(res)

    for rep in res:
        print(f"Project nanme: {rep['name']}")
        print(f"Project url: {rep['svn_url']}")
except Exception as e:
    print("Please enter a valid username")
