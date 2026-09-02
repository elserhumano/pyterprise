#!/usr/bin/python3

import os
import pyterprise
import time
from datetime import date

# Config
tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)

today = date.today()
today_str = today.strftime("%Y/%m/%d")

avoid_orgs = [ 'My-Company-POD-DEV',
               'My-Company-POD',
               'My-Company-Networks',
               'My-Company-Networks-Shared'
             ]

allow_orgs = [ 'My-Company-POD-DEV'
             ]

allow_varsets = [ 'FR-VRAPPRD_ZS1_VAR_SET'
                ]

# Read values from external file
account_values = {}
with open("token_values.txt", "r") as f:
    for line in f:
        if "=" in line:
            k, v = line.strip().split("=", 1)
            account_values[k] = v


for org in client.list_organizations():
    # The next if it's just to debug and for specific organization name
    # To use with all the orgs just comment the following line
    #if org.name not in avoid_orgs:
    if org.name in allow_orgs:
        for varset in org.list_varsets():
            # The next if it's just to debug and for specific variable set name
            # To use checking all the variable set names disable the following line
            #if varset.name == 'POD_SG_MGMT_VAR_SET':
            if varset.name in allow_varsets:
                for variable in varset.list_set_variables():
                    if variable.key in ["refresh_token", "vra_refresh_token"]:
                        pre_variable_desc = variable.description
                        account_id = pre_variable_desc.split()[0] if pre_variable_desc else None
                        # Here I need to check if the variable to change exists or not
                        if account_id in account_values:
                            token_value = account_values.get(account_id)
                            print(f"=======================================================================")
                            print(f"Org: {org.name}, Varset: {varset.name}, Var: {variable.key}")
                            print(f"Account: {account_id}, Token found: {'YES' if token_value else 'NO'}")
                            print(f"Description: {pre_variable_desc}")
                            print ('')
                            print ('Removing ', variable.key, ' from varset: ', varset.name)
                            varset.remove_variable_from_set(variable.id)

                            # Now I need to recreate with the new values
                            the_desc = account_id + " " + today_str + " updated by script:  " + today_str
                            print ('')
                            the_variable = 'TF_VAR_refresh_token'
                            print ('Add ', the_variable, ' with a new value')
                            print ('The token: ', token_value)
                            print ('Description: ', the_desc)
                            varset.add_variable_to_set_ext(the_variable, token_value, the_desc, 'env', False, True)
                            print ('')
                        else:
                            print ('The vRA account not in the list to remove')

