import time
# System monitoring states
connection_active = True # Network connection status
data_received = False #data transfer status
system_ready = True # System readiness status

# Status_check
if connection_active:
    print("Connection established.")
if not data_received:
    print("wating for data...")
time.sleep(5) 
print("Data received.")
