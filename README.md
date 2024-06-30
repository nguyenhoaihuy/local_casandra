# Introduction
Just a local cluster to deploy canssandra on

# How to deploy a cluster with 2 nodes with Kind
kind create cluster --config kind-config.yaml

# How to get the list of cluster
kind get clusters

# How to delete a cluster using kind
kind delete cluster --name <name_of_a_cluster>