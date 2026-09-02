#!/usr/bin/python3

import os
import re
import pyterprise

tfe_token = os.getenv('TFE_TOKEN')
tfe_url   = os.getenv('TFE_URL')
tfe_org   = os.getenv('TFE_ORG')

client    = pyterprise.Client()
client.init(token=tfe_token, url=tfe_url)
org = client.set_organization(id=tfe_org)
orgs = client.list_organizations()

excluded_orgs = [ 'My-Company-CoreIT',
                  'My-Company-Networks',
                  'My-Company-Networks-Shared',
                  'My-Company'
                ]

included_orgs = [ 'My-Company-POD' 
                ]

included_ws =   [ 'pod_de_win_workplace_pvdsvd-mod-prod'
                ]

included_modules = [ 'vm-v2-supermodule',
                     'onboarding-vm',
                     'vm-v2-localad',
                     'vm-v2-bis-supermodule',
                     'vms-v2-bis1-gad',
                     'vm-v2-gad-supermodule'
                   ]

for org in orgs:
    if org.name not in excluded_orgs:
    #if org.name in included_orgs:
        ###print ('========================================================================================')
        ###print ('Organization: ', org.name)
        ###print ('')
    
        for the_ws in org.list_workspaces():
            #if the_ws.name in included_ws:
                the_project_name = ''
                for the_var in the_ws.list_variables():
                     if the_var.key == "project_name":
                          the_project_name = the_var.value
                the_list = []
                for r in the_ws.list_resources2():
                    #print (r.module)
                    if r.module.startswith(tuple(included_modules)):
                        ## for debug print ('ID: ', r.id, '\nAddress: ', r.address, '\nName: ', r.name, ' \nProvider: ', r.provider, ' \nModule: ', r.module, ' \nProvider Type: ', r.provider_type)
                        ## for debug print ('')
                        process_name_server = re.search (r'"([^"]+)"', r.address)
                        if process_name_server:
                            get_name_server = process_name_server.group(1)
                        if get_name_server not in the_list:
                            the_list.append(get_name_server)
                    
                the_output = org.name + ',' + the_ws.name + ',' + the_project_name + ',' + str(len(the_list))
                print (the_output)


