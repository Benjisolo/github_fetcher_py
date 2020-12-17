import requests
from github import Github

ACCESS_TOKEN = "5c5090760730994bf483bf0d8b6b79f789a6c7be"
headers = {'Authorization' : 'token ' + ACCESS_TOKEN}
USER_END_POINT = 'https://api.github.com/users'
# Reading the Input file
with open('user-info') as f:
    # Creating/Openning the Output file
    fdata = open('data.txt', 'w')
    fdata = open('data.txt', 'a')
    # Reading each line of the Input file
    for index, line in enumerate(f):
        username = line.strip()
        # Fetching the user contained in the line read
        response = requests.get(f'{USER_END_POINT}/{username}', headers = headers)
        # If the User's data found
        if response.status_code == 200:
            resp = response.json()
            followers_nbr = resp['followers']
            following_nbr = resp['following']
            # Fetching User's "followers"
            fdata.write(f'\n{index+1}) {username}:\n  \'Followers\' [{followers_nbr}]: "')
            if followers_nbr > 0:
                resp_followers = requests.get(f'{USER_END_POINT}/{username}/followers?per_page=100', headers = headers)
                r1 = resp_followers.json()
                for i in range(len(r1)):
                    fdata.write(f'{i+1}. {r1[i]["login"]}; ')
            # Fetching User's "following"
            fdata.write(f'"\n  \'Following\' [{following_nbr}]: "')
            if following_nbr > 0:
                resp_following = requests.get(f'{USER_END_POINT}/{username}/following?per_page=100', headers = headers)
                r2 = resp_following.json()
                for i in range(len(r2)):
                    fdata.write(f'{i+1}. {r2[i]["login"]}; ')
            fdata.write('"\n')
        # If User's data not found
        else :
            fdata.write(f'\n{index+1}) {username} : DATA NOT FOUND FOR THIS USER!\n')
    fdata.close()