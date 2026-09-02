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

print('Organizations: ')
print('')
for org in orgs:
    print(org.name)
    print ('')
    for agpool in org.list_agent_pools():
        print ('Agent Pool ID: ', agpool.id, ' Name: ', agpool.name)
        for agent in agpool.list_agents():
            print ('Agent Name: ', agent.name, ' Status: ', agent.status)

    print ('.................................................')

