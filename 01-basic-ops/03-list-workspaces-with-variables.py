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
for workspace in org.list_workspaces():
  print('========================================================================================')
  print('Organization: ', org.name)
  print('Workspace: ', workspace.name)
  #print(workspace.name)
  # Print a list of the variables
  print('List of variables: ')
  for variable in workspace.list_variables():
    print(" -> ", variable.key, variable.value)
