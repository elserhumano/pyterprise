#!/usr/bin/python3

import os
import pyterprise

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)
org = client.set_organization(id=tfe_org)

# Print a list of workspaces with only the name
print('Organization: ', org.name)
print('')
print('Workspaces: ')
for workspace in org.list_workspaces():
  #print(' -> ', workspace.name)
  print(workspace.name)
