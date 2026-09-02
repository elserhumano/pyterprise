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

# For each org:
#   Change the value of the variable netbox_server_url from the varset GLOBAL_VAR_SET
#     Actual value is current_value and will be new_value

# This is the varset where the current value is in the variable
in_varset = 'GLOBAL_VAR_SET'

# This is the variable to change in the varset mentioned above
variable_to_change = 'netbox_server_url'

# The current value
current_value = 'https://netbox-prod.medc.mgmt.mycompany.intranet'

# The new value will be...
new_value = 'bleble'

# Loop in all the organizations, then get only the specific VARSET
for org in client.list_organizations():
    print ("Checking org: ", org.name) ## For debugging
    for varset in org.list_varsets():
        print ("....Checking VARSET: ", varset.name) ## For debugging
        #print ("....Checking VARSET: ", varset) ## For debugging
        #print ("....Checking VARSET: ", varset.id) ## For debugging
        if varset.name == in_varset:
            print ("----Found ", in_varset)
            for variable_set in varset.list_set_variables():
                print ("--------Checking variable set: ", variable_set.key, "with value: ", variable_set.value)
                if variable_set.key == variable_to_change and variable_set.value == current_value:
                    print ("========Found ", variable_set.key)
                    # Here I will check if the value is the current and then proceed to change.
                    # First remove the variable:
                    the_variable = variable_set.key
                    print ('')
                    print ('Removing ', the_variable, ' from varset: ', varset.name, 'in Org: ', org.name)
                    print ('-------------------------------------------')
                    print ('-> Variable: ',variable_set.key)
                    #varset.remove_variable_from_set(variable_set.id)
                    # Now I need to recreate with the new values
                    the_desc = "Updated by script:  " + today_str
                    print ('')
                    print ('Add ', the_variable, ' with a new value')
                    print ('The new value: ', new_value)
                    print ('Description: ', the_desc)
                    #varset.add_variable_to_set_ext(the_variable, new_value, the_desc, 'terraform', False, False)
                    print ('')
                    print ('.................................................')
                    print ('')
                    break
            break
