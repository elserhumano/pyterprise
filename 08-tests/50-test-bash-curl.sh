#!/bin/bash

export TFE_SERVER="https://tfe.my-company-cloud.com"
export TFE_TOKEN="j9AVlroOIFzUkw.atlasv1.qa4w6ENhUzYF0Fqy2g3w4pyyfJ1WkTdC40BstPn0Hn7lYumOj222dgfSX8EnaL7fyTM"
export TFE_ORG="My-Company-POD-DEV"


curl \
-vv \
--header "Autorization: Bearer j9AVlroOIFzUkw.atlasv1.qa4w6ENhUzYF0Fqy2g3w4pyyfJ1WkTdC40BstPn0Hn7lYumOj222dgfSX8EnaL7fyTM" \
--header "Content-Type: application/vnd.api+json" \
"https://tfe.my-company-cloud.com/api/v2/vars?filter%5Borganization%5D%5Bname%5D=My-Company-POD-DEV&filter%5Bworkspace%5D%5Bname%5D=ago_fr_developer-dev"



#"$TFE_SERVER/api/v2/vars?filter%5Borganization%5D%5Bname%5D=My-Company-POD-DEV&filter%5Bworkspace%5D%5Bname%5D=ago_fr_developer-dev"

#--header "Autorization: Bearer $TFE_TOKEN" \

# "$TFE_SERVER/api/v2/vars?filter%5Borganization%5D%5Bname%5D=MY-ORG-DEV&filter%5Bworkspace%5D%5Bname%5D=pod_fr_lin_service-prod"

