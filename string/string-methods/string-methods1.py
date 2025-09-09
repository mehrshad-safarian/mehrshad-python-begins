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

customer_name = 'john smith'
account_number = '12345'
account_balance = 5250.75
print('Customer Profile: %s, Account: %s' % (customer_name, account_number))

report_line = 'name: {0},Balance: ${1}'.format(customer_name,account_balance)
print(report_line)

status = 'Account: {}, Ststus: {}'.format(account_number, 'Active')
print(status)

revenue = 123456787.89023
formatted_revenue = 'Total Revenue: ${:,.2f}'.format(revenue)
print(formatted_revenue)
