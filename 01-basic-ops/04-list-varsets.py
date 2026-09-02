#!/usr/bin/python3

import os
import pyterprise

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)
org = client.set_organization(id=tfe_org)

print ('Organization: ', tfe_org)
print ('')
print ('Variable Sets: ')
# Print a list of varsets with only the name
for varset in org.list_varsets():
    #print(' =>  ', varset.name, ' ... ', varset.id)
    print (' => ', varset.name)
