#!/usr/bin/python3

import os
import sys
import re
import ast
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
        # To get the opco_trigram value
        opco_trigram = ''
        dicc = {} 
        for the_varset in org.list_varsets():
            for the_var_set in the_varset.list_set_variables():
                if the_var_set.key == "opco_trigram":
                    opco_trigram = the_var_set.value
                    attrs_dict = ast.literal_eval(str(the_varset.attributes))
                    is_global = attrs_dict.get("global", False)
                    if is_global:
                        # print ("Is global: ", is_global)
                        # print ('VarSet: ',the_varset.name)
                        # print ('El varset es global a wks y projects')
                        total_list = org.list_workspaces()
                        for the_item4 in total_list:
                            dicc[the_item4.id] = opco_trigram
                    else:
                        list_wks = the_varset.list_ws()
                        list_pro = the_varset.list_pr()
                        list_wks_pro = []
                        # print ('List of wks from varsets: ', list_wks)
                        # print ('')                                
                        # print ('List of projects: ', list_pro)
                        # print ('')
                        for the_proj in list_pro:
                            for the_proj_org in org.list_projects():
                                if the_proj == the_proj_org.id:
                                    for add_item in the_proj_org.list_ws():
                                        list_wks_pro.append(add_item.id)
                        #print ('List of wks from projects: ', list_wks_pro)
                        total_list = []
                        for the_item in list_wks:
                            total_list.append(the_item)
                        for the_item2 in list_wks_pro:
                            if the_item2 not in total_list:
                                total_list.append(the_item2)
                        for the_item3 in total_list:
                            dicc[the_item3] = opco_trigram


        for the_ws in org.list_workspaces():
            if the_ws.name not in excluded_ws:
                the_project_name = ''
                for the_var in the_ws.list_variables():
                        if the_var.key == "project_name":
                            the_project_name = the_var.value
                        if the_var.key == "opco_trigram":
                            dicc[the_ws.id] = the_var.value
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

                if the_ws.id in dicc:
                    the_opco = dicc[the_ws.id]
                else:
                    the_opco = ''

                the_output = org.name + ',' + the_ws.name + ',' + the_project_name + ',' + the_opco + ',' + str(len(the_list))
                print (the_output)
