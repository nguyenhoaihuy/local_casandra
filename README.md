# Introduction
Just a local cluster to deploy canssandra on

# How to deploy a cluster with 2 nodes with Kind
```kind create cluster --config kind-config.yaml```

# How to get the list of cluster
```kind get clusters```

# How to delete a cluster using kind
```kind delete cluster --name <name_of_a_cluster>```

# How to deploy cassandra on cluster
```kubectl apply -f cassandra.yaml```

# Expose external access using NodePort service
```kubectl apply -f cassandra-service.yaml```.
NodePort will load balance via kube-proxy (Round-robin)

# Run example
## Check if the cluster is up and running
```python3 test_connection.py```

## Load test

# Debug
## Kind bridge docker network cannot access internet
Misconfiguration on host. Add 8.8.8.8 and 8.8.4.4 DNS server to /etc/resolv.conf on linux host
## NodePort is not working
NodePort was created improperly. Selector should be app_lable instead of statefulSet name


