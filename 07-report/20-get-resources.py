#!/usr/bin/python3

import os
import sys
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

excluded_var_sets = [ 'Artifactory Variables',
                      'Vault Variables'
                    ]

excluded_ws = [ 'cloudbroker-management-zone-prod'
              ]

for org in orgs:
    if org.name not in excluded_orgs:
    #if org.name in included_orgs:
        veces = 0 
        for the_ws in org.list_workspaces():
            if the_ws.name not in excluded_ws:

                # To get the opco_trigram value
                opco_trigram = ''
                for var_set in org.list_varsets():
                        if var_set.name not in excluded_var_sets:
                            list_of_wks_from_varset = []
                            list_of_wks_from_varset = var_set.list_ws()
                            print ('Org: ', org.name, ' Wks: ', the_ws.name, ' VarSet: ', var_set.name, ' List of wks in varset: ', var_set.list_ws())
                            if var_set.list_ws():
                                for ws_var_set in var_set.list_ws():
                                    #print ('Workspace from varset workspace list: ', ws_var_set)
                                    #print ('Workspace in count:                   ', the_ws.id)
                                    if ws_var_set == the_ws.id:
                                        for var_set_variable in var_set.list_set_variables():
                                            if var_set_variable.key == "opco_trigram":
                                                opco_trigram = var_set_variable.value
                                                print ('---------------------------------')
                                                print ('Workspace: ', the_ws.name)
                                                print ('VarSet Name: ', var_set.name)
                                                print ('Set opco_trigram to: ', opco_trigram)
                                                print ('Variable VarSet: ', var_set_variable.key)
                                                print ('')
                                                break
                                            else:
                                                print ('============================')
                                                print ('Workspace: ', the_ws.name)
                                                print ('VarSet Name: ', var_set.name)
                                                print ('Opco Trigram: ', opco_trigram)
                                                print ('Variable VarSet: ', var_set_variable.key)
                                                print ('')
                                    else:
                                        print ('No son iguales')
                                        print ('ws_var_set: ', ws_var_set, ' the_ws.id: ', the_ws.id)
                                        print ('') 


                the_project_name = ''
                for the_var in the_ws.list_variables():
                     if the_var.key == "project_name":
                          the_project_name = the_var.value
                the_list = []
                for r in the_ws.list_resources2():
                    #print (r.module)
                    if r.module.startswith(tuple(included_modules)):
                        ## For debug!
                        ## print ('ID: ', r.id, '\nAddress: ', r.address, '\nName: ', r.name,)
                        ## print (' \nProvider: ', r.provider, ' \nModule: ', r.module, ' \nProvider Type: ', r.provider_type)
                        ## print ('')
                        process_name_server = re.search (r'"([^"]+)"', r.address)
                        if process_name_server:
                            get_name_server = process_name_server.group(1)
                        if get_name_server not in the_list:
                            the_list.append(get_name_server)
                    
                the_output = org.name + ',' + the_ws.name + ',' + the_project_name + ',' + opco_trigram + ',' + str(len(the_list))
                print (the_output)
                print ('....................................')
                if opco_trigram == '' and veces == 3:
                    sys.exit()

                veces = veces + 1
