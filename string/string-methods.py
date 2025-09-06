log_entry = "Error 404: File not found at /var/www/html/index.php"
error_position = log_entry.find("Error")
file_position = log_entry.find("/var")

file_path = "C:\\User\\Documents\\config.txt"
unix_path = file_path.replace("\\", "/")

server_log_entry = 'server01,warning,disk_space_low,2024-01-15'
components = server_log_entry.split(',')
print(components)

username = 'Admin_user'
standardized_username = username.lower()

employee_id = 'EMP123'
is_valid = employee_id.isalpha()

config_line = 'db_host=localhost:5432\n'
clean_config = config_line.rstrip()
print(clean_config)

raw_config = 'db_host=localhost:5432   \n'
host_value = raw_config.rstrip().split('=')[1]
print(host_value)