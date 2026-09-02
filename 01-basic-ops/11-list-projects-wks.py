#!/usr/bin/python3

import os
import pyterprise

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)
org = client.set_organization(id=tfe_org)

# Print a list of projects only the name
print('Organization: ', org.name)
print('')
print('Projects: ')
for pr in org.list_projects():
    print(pr.name)
    print ('Workspaces: ')
    for wks in pr.list_ws():
        print(wks.name)

