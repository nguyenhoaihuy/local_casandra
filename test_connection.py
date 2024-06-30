from cassandra.cluster import Cluster

cluster = Cluster(['172.18.0.4'], port=30183)  # 'cassandra' is the Kubernetes service name
session = cluster.connect()
# Query system tables to get rpc_address
query = "SELECT rpc_address FROM system.local"

# Execute query
rows = session.execute(query)
# Print rpc_address for each node
for row in rows:
    print(f"RPC Address: {row.rpc_address}")
