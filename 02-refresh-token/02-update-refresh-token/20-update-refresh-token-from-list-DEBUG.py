#!/usr/bin/python3

import os
import pyterprise
import time
from datetime import date

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)

today = date.today()
today_str = today.strftime("%Y/%m/%d")

# Update refresh token getting from a list in a file

# Read the file and put that in memory

accounts_from_file = []
with open ("./refresh_token_to_update.txt") as file:
    for account in file:
        the_line = account.replace(" ", "")
        accounts_from_file.append(the_line)


for org in client.list_organizations():
    print ("Checking org: ", org.name) ## For debugging
    for varset in org.list_varsets():
        print ("Checking VARSET: ", varset.name) ## For debugging
        for variable_set in varset.list_set_variables():
            #if (variable_set.key == "refresh_token" or variable_set.key == "vra_refresh_token") and org.name == 'My-Company-POD-DEV':
            if (variable_set.key == "refresh_token" or variable_set.key == "vra_refresh_token"):
                # The account to check
                if variable_set.description is None:
                    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print ("Empty description here-> Org: ", org.name," VARIABLE SET: ", varset.name, " variable: ", variable_set.key)
                    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    get_the_account = ""
                else:
                    get_the_account = variable_set.description.split(" ",1)[0]
                for x in accounts_from_file:
                    print ("Debugging error: ", x)
                    the_account = x.split(",", 1)[0]
                    the_date = x.split(",", 2)[1]
                    pre_token = x.split(",", 2)[2]
                    the_token = pre_token.replace("\n", "")
                    if get_the_account == the_account:
                        print ("Here will be changed: ", get_the_account, " in VARSET: ", varset.name, " Org: ", org.name)
                        # First I will need to delete the previous refresh_token variable
                        the_variable = variable_set.key
                        print ('')
                        print ('Removing ', the_variable, ' from varset: ', varset.name)
                        print ('-------------------------------------------')
                        print ('-> Variable: ',variable_set.key)
                        print ('Here will execute this: varset.remove_variable_from_set(variable_set.id)')
                        # Now I need to recreate with the new values
                        the_desc = the_account + " " + the_date + " updated by script:  " + today_str
                        print ('')
                        print ('Add ', the_variable, ' with a new value')
                        print ('The token: ', the_token)
                        print ('Description: ', the_desc)
                        print ("Here will execute this: varset.add_variable_to_set_ext(the_variable, the_token, the_desc, 'terraform', False, True)")
                        print ('')
                        print ('.................................................')
                        print ('')


