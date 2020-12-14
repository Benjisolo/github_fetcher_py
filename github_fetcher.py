import requests
from github import Github
ACCESS_TOKEN = "5c5090760730994bf483bf0d8b6b79f789a6c7be"
headers = {'Authorization' : 'token ' + ACCESS_TOKEN}
END_POINT = 'https://api.github.com/users'

with open('user-info') as f:
    fdata = open('data.txt', 'w')
    fdata = open('data.txt', 'a')
    for index, line in enumerate(f):
        username = line.strip()
        response = requests.get(f'{END_POINT}/{username}', headers = headers)
        if response.status_code == 200:
            r = response.json()
            followers = r['followers']
            following = r['following']
            fdata.write(f'{index}- {username} : Followers = {followers}, Following = {following}\n')
        else :
            fdata.write(f'xxx {index}- {username} : DATA NOT FOUND FOR THIS USER! xxx')
    fdata.close()