#!/usr/bin/env python

import requests
import json

requests.packages.urllib3.disable_warnings()
response = requests.get('https://api.craft.htb/api/auth/login',  auth=('dinesh', '4aUh0A8PbVJxgd'), verify=False)
json_response = json.loads(response.text)
token =  json_response['token']
print(response)
print(token)

headers = { 'X-Craft-API-Token': token, 'Content-Type': 'application/json'  }
response = requests.get('https://api.craft.htb/api/auth/check', headers=headers, verify=False)
print(response.text)
