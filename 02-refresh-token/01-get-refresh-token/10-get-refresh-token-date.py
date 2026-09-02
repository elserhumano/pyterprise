#!/usr/bin/python3

import os
import pyterprise

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)

list_accounts = []

print()
print ("Enter the year: ")
the_year_input = input()
print()
print ("Enter the month (01...12): ")
the_month_input = input()
print()
print ("Starting the process...")
print()

the_date_input = the_year_input + "-" + the_month_input

print ("Process ALL except MY-ORG-DEV for this date: ", the_date_input)
print ()

for org in client.list_organizations():
    for varset in org.list_varsets():
        for variable in varset.list_set_variables():
            if variable.key == "refresh_token" and org.name != 'My-Company-DEV':
                # The dates to check
                #if "2024-07" not in variable.description and "2024-09" not in variable.description:
                #print ("Procesing Org:", org.name, " Varset: ", varset.name)
                #if "2024-07" not in variable.description:
                if the_date_input in variable.description:
                    print (org.name,',',varset.name,',',variable.key,',',variable.description)
                    the_element = variable.description.split(" ", 1)[0]
                    if the_element not in list_accounts:
                        list_accounts.append(the_element)

print()
for x in sorted(list_accounts):
    print (x)

