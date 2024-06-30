from cassandra.cluster import Cluster

cluster = Cluster(['172.18.0.1'], port=30183)  # 'cassandra' is the Kubernetes service name
session = cluster.connect()
