import re

log_entry = "ERROR [2024-01-02 15:30:45] Connection timeout in database"
print("Our log entry:", log_entry)

pattern = r'ERROR \[(.*?)\] (.*)'
match = re.search(pattern, log_entry)

print("Timestamp:", match.group(1))
print("Error message:", match.group(2))