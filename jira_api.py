# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:58:37 2024

@author: NXP
"""

import requests
import pandas as pd

bearer_token = 'your token'
base_url = 'https://servicedesk.ninjavan.co'

# Authentication headers
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Accept': 'application/json'
}

# Endpoint for getting issues
endpoint = f'{base_url}/rest/servicedeskapi/request/BIID-3922' #your endpoint, this sample pulls information of 1 ticket with id BIID-3922.

# Make GET request
response = requests.get(endpoint, headers=headers)
print(response)
# Check response status
if response.status_code == 200:
    # Extract issues from response
    print(response.json())

else:
    print('Failed to retrieve issues:', response.text)
