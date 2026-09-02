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
# Print a list of teams with only the name
for the_user in org.list_users():
    print('Email: ', the_user.attributes.email, ' Status: ', the_user.attributes.status, ' ID: ', the_user.id)
    #print (the_user)
    #print ('')

