#!/usr/bin/python3

import os
import pyterprise

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)

# For each org:
#   Remove the variable 'nebox_server_url' from the all network variable sets there.
#   Add the variable 'nebox_server_url' to the varset GLOBAL_VAR_SET


# Debug only with the Org: My-Company-POD-DEV
tfe_org = 'My-Company-POD-DEV'
org = client.set_organization(id=tfe_org)

varset_to_remove = 'NETWORK'
varset_to_add = 'GLOBAL_VAR_SET'

variable_to_move = 'netbox_server_url'
value_to_move    = 'https://netbox-prod.medc.mgmt.mycompany.intranet'

for varset in org.list_varsets():
    # if the varset contain varset_to_remove in the name => remove the variable: "netbox_server_url" in this varset
    # if the varset contain varset_to_add in the name => add the variable: 
    #    "netbox_server_url" with this content: "https://netbox-prod.medc.mycompany.intranet" in this varset

    list_variables = []
    dict_variables = {}
    for variable_set in varset.list_set_variables():
        list_variables.append(variable_set.key)
        dict_variables[variable_set.key] = variable_set.id

    #Debug
    #print ('..................................................')
    #print ('Checking varset: ', varset.name)
    #print ('List variables of varset: ', list_variables)
    #print (dict_variables)

    print ('Processing org: ', org.name, ' VarSet: ', varset.name)

    if varset_to_remove in varset.name and variable_to_move in dict_variables:
        print ('')
        print ('Removing from varset: ', varset.name)
        print ('-------------------------------------------')
        print ('-> Variable: ',variable_to_move, ' => Value: ', dict_variables[variable_to_move])
        varset.remove_variable_from_set(dict_variables[variable_to_move])
        print ('')
        print ('.....................................................')
    elif varset_to_add in varset.name and variable_to_move not in dict_variables:
        print ('')
        print ('Adding in varset: ', varset.name)
        print ('-------------------------------------------')
        print ('-> Variable: ', variable_to_move, ' => Value: ', value_to_move)
        varset.add_variable_to_set(variable_to_move, value_to_move)
        print ('')
        print ('.....................................................')

