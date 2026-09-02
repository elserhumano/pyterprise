#!/usr/bin/python3

import os
import pyterprise

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)
org = client.set_organization(id=tfe_org)

print ('========================================================================================')
print ('Organization: ', tfe_org)
print ('')
# Print a list of varsets with only the name
for varset in org.list_varsets():
    print('Variable Set: ', varset.name, ' -> ', varset.id)
    print ('')
    print ('Variables: ')
    print ('')

    for variable in varset.list_set_variables():
        #print (variable)
        print (" => ", variable.key, ' = ', variable.value, 'description: ', variable.description)
    print ('-----------------------------------------------------------------------------------')

