#!/usr/bin/python3

import os
import pyterprise

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)
org = client.set_organization(id=tfe_org)

orgs = client.list_organizations()

sel_orgs = [
            "My-Company-Branch15",
            "My-Company-Branch16",
            "My-Company-Branch17",
            "My-Company-Branch18"
           ]

exclude_varsets = [
                    "Artifactory Variables",
                    "Vault Variables"
]


check_vars = [
                "mapZoneLB",
                "zonesMap"
]


for org in orgs:

    #Check if the org is the org required

    if org.name in sel_orgs:
        print ('')
        print ('========================================================================================')
        print ('Organization: ', org.name)
        print ('')

        # Get a list of varsets with only the name
        for varset in org.list_varsets():

            #Setup here condition to get the orgs required
            if varset.name not in exclude_varsets:
                print('Variable Set: ', varset.name, ' -> ', varset.id)
                print ('')
                print ('Variables: ')
                print ('')

                for variable in varset.list_set_variables():
                    #print (variable)
                    if variable.key in check_vars:
                        print (" => ", variable.key, ' = ', variable.value, 'description: ', variable.description)

                print ('-----------------------------------------------------------------------------------')
                print ('')

