#!/bin/bash

curl --noproxy "*" --header "Autorization: Bearer $TFE_TOKEN" --header "Content-Type: application/vnd.api+json" --request GET https://tfe.my-company-cloud.com/app/MY-ORG-DEV/settings/varsets/varset-uevqtPYTy5uGi7sj


