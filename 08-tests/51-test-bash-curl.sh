#!/bin/bash

export TFE_SERVER="https://tfe.my-company-cloud.com"
export TFE_TOKEN="j9AVlroOIFzUkw.atlasv1.qa4w6ENhUzYF0Fqy2g3w4pyyfJ1WkTdC40BstPn0Hn7lYumOj222dgfSX8EnaL7fyTM"
export TFE_ORG="My-Company-POD-DEV"

# Get general info from orgs
#curl -k -v --noproxy "*" --header "Autorization: Bearer j9AVlroOIFzUkw.atlasv1.qa4w6ENhUzYF0Fqy2g3w4pyyfJ1WkTdC40BstPn0Hn7lYumOj222dgfSX8EnaL7fyTM" --header "Content-Type: application/vnd.api+json" --request GET https://tfe.my-company-cloud.com/api/v2/organizations\?page\[number\]\=1\&page\[size\]\=20

# Show Variable Set from a org
curl -k -v --noproxy "*" --header "Autorization: Bearer j9AVlroOIFzUkw.atlasv1.qa4w6ENhUzYF0Fqy2g3w4pyyfJ1WkTdC40BstPn0Hn7lYumOj222dgfSX8EnaL7fyTM" --header "Content-Type: application/vnd.api+json" --request GET https://tfe.my-company-cloud.com/api/v2/varsets/varset-XSqkXBxrKcuqSncE


