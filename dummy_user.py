# Generate fake user details 

import requests

def fake_details():
    r = requests.get('https://api.randomuser.me/')
    return r.json()['results'][0]

def show(r):
    print('Name:', r['name']['first'], r['name']['last'])
    print('Email:', r['email'])
    print('Username:', r['login']['username'])
    print('Password:', r['login']['password'])

if __name__ == '__main__':
    a = fake_details()
    show(a)