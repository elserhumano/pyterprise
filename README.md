### pyterprise

# Terraform API Documentation

https://developer.hashicorp.com/terraform/cloud-docs/api-docs/variable-sets

# Process:

- Execute 00 first to setup the env variables.

If you want to get a list with the tokens that will expire in some month without MY-ORG-DEV org:
  - Execute 10

If you want to get a list with the tokens that will expire in some month only in MY-ORG-DEV org:
  - Execute 11

If you want to get a list of ALL tokens in All orgs:
  - Execute 12

# Files:

00-Tfe-token.sh
  - Setup Env variables for the rest of the python scripts.

01-list-orgs.py
  - List all the organizations (where you have access).

02-list-workspaces.py
  - List all the workspaces of an organization.

03-list-workspaces-with-variables.py
  - List all the variables of a workspace of an organizaton.

04-list-varsets.py
  - List all the variable sets of an organization.

05-get-variables-varset.py
  - List all the variables inside a varset, the output is: name of the variable, his value and description.

10-get-refresh-token-date.py
  - List all the refresh tokens of all orgs except MY-ORG-DEV asking first for a date (it's the date in the description of the refresh token variable).

11-get-refresh-token-date-POD-DEV.py
  - It's the same that the previous one but this time only for MY-ORG-DEV asking first for a date (it's the date in the description of the refresh token variable). 

12-get-all-refresh-token-all-orgs-without-dates.py
  - List all the refresh token in all organizations without specify a date.

15-get-all-refresh-token-agopoddev-without-dates.py
  - List all the refresh token in only MY-ORG-DEV org without specify a date.

20-move-variable-varset.py
  - Moving variable from a varset to another one, this means that get the value, delete from the original varset, and finally add to the destination varset. This is for debug in MY-ORG-DEV and with ficticious variable sets (FERFER).

30-prod-move-variable-varset.py
  - Similar to the previous but this time is in production.

40-update-refresh-token-from-list-ALL.py
  - Update the refresh token in all the organizations getting the values from an external file in the same directory with the name refresh_token_to_update.txt.

50-update-refresh-token-from-list-DEBUG.py
  - The same that the previous but this only run without make any modifications and let you know the proposed changes, this is only for DEBUG and PRE-CHECK.

_50-vra-tests.py
  - Was a POC to find an easy way to get the refresh token directly from vRA API without use the workspaces management token. By now is FREEZE.

60-update-variable-varset.py
  - Update the value of a specific variable that's member of a specific variable set.

