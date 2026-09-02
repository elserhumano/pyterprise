#!/bin/bash
pushd pyterprise
pushd pyterprise-0.0.15
. 01-uninstall-pyterprise.sh
. 02-install-pyterprise.sh
. 03-check-pyterprise.sh
popd
popd


