# Introduction
Just a local cluster to deploy canssandra on

# How to deploy a cluster with 2 nodes with Kind
kind create cluster --config kind-config.yaml

# How to get the list of cluster
kind get clusters

# How to delete a cluster using kind
kind delete cluster --name <name_of_a_cluster>

# Debug
## Kind bridge docker network cannot access internet
Misconfiguration on host. Add 8.8.8.8 and 8.8.4.4 DNS server to /etc/resolv.conf on linux host

