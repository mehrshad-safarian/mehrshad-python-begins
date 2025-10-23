server_metrics = [["CPU_usage", "RAM_usage", "Disk_space"],
               ["Network_in", "Network_out", "Active_connections"],
                ["Response_time", "Error_rate", "Queue_length"]]
resource_Metrics = server_metrics[0]
print(resource_Metrics)
network_in = server_metrics[1][0]
print(network_in)