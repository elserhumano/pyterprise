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

# Unlock all the workspaces for maintenance in a specific org

# Read the file and put that in memory
orgs_for_maintenance = []
with open ("./orgs_for_maintenance.txt") as file:
    for account in file:
        the_line = account.replace(" ", "")
        the_line = account.replace("\n", "")
        orgs_for_maintenance.append(the_line)

for org in client.list_organizations():
    print ("Checking org: ", org.name) ## For debugging
    if (org.name in orgs_for_maintenance):
      print ('Unlock this entire org: ', org.name)
      print ('Unlocking workspaces')
      for the_ws in org.list_workspaces():
          print ('Unlock workspace: ', the_ws.name)
          the_ws.unlock ("In maintenance back later.")
    #break
