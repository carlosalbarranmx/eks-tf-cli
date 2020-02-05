#!/bin/sh
#set -e
#aws eks update-kubeconfig --name example-cluster
#kubectl create clusterrolebinding cluster-system-anonymous --clusterrole=cluster-admin --user=system:anonymous
# Retrieve token with Heptio Authenticator
TOKEN=$(heptio-authenticator-aws token -i example | jq -r .status.token)
# Output token as JSON
jq -n --arg token "$TOKEN" '{"token": $token}'
