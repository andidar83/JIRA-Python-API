# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:58:37 2024

@author: NXP
"""

import requests
import pandas as pd
# # Jira credentials
# username = 'andi.darmawan@ninjavan.co'
# api_token = 'NjIzOTQ5MzIzMDIxOop1cwJ5KiXZAfWOPRJYv4J0hz0o'
# base_url = 'https://servicedesk.ninjavan.co'

# # Authentication
# auth = (username, api_token)

# # Endpoint for getting issues
# endpoint = f'{base_url}/rest/servicedeskapi/request'

# response = requests.get(endpoint, auth=auth)

# print(response)
# print(response.text)


# Jira credentials
bearer_token = 'NjIzOTQ5MzIzMDIxOop1cwJ5KiXZAfWOPRJYv4J0hz0o'
base_url = 'https://servicedesk.ninjavan.co'

# Authentication headers
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Accept': 'application/json'
}

jql_query = 'project = "ID Business Intelligence"'

# Construct the URL with the JQL query
endpoint = f'{base_url}/rest/api/2/search?jql={jql_query}'

# Make GET request
response = requests.get(endpoint, headers=headers)
print(response)
# Check response status
if response.status_code == 200:
    # Extract issues from response
    print(response.json())


else:
    print('Failed to retrieve issues:', response.text)

# # Parameters for pagination
# start_at = 0
# max_results = 50  # Adjust as needed

# # List to store all issues
# all_issues = []

# while True:
#     # Parameters for pagination
#     params = {
#         'startAt': start_at,
#         'maxResults': max_results
#     }

#     # Make GET request
#     response = requests.get(endpoint, auth=auth, params=params)

#     # Check if request was successful
#     if response.status_code == 200:
#         # Extract issues from response
#         issues = response.json()['issues']
        
#         # Add issues to the list
#         all_issues.extend(issues)
        
#         # Increment startAt for pagination
#         start_at += max_results
        
#         # Break the loop if all issues have been retrieved
#         if len(issues) < max_results:
#             break
#     else:
#         print('Failed to retrieve issues:', response.text)
#         break

# # Print all issues
# for issue in all_issues:
#     print(issue)
