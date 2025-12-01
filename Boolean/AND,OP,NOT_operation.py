# ADD
# Authentication system operation example 
has_username = True      # User has entered a username
has_password = True      # User has entered a password
# Both must be True for credentials to be considered valid
credentials_valid = has_username and has_password
# Security check example 
is_authenticated = True   # User has successfully logged in
has_permissions  = False   # User has the required permissions/role
# User must be authenticated AND have permissions to access the system
can_access = is_authenticated and has_permissions
# Output results
print(f"Credentials valid: {credentials_valid}")   # Shows if login info is complete
print(f"Access granted: {can_access}")            # Shows if user is allowed to access
# ADD
print()

# OR
# Login methods 
has_password = False
has_fingerprint = False
can_login = has_password or has_fingerprint

# Backup systems status
primary_running = False
backup_active = True 
system_available = primary_running or backup_active 

# Output results
print(f"Can login: {can_login}")                 # True if either method is available
print(f"System available: {system_available}")   # True if either system is operational
# OR
print()

# NOT
# System maintenance check
is_maintenance = True
is_available = not is_maintenance

# Process status
is_busy = False
can_process = not is_busy

# Output results
print(f"System available: {is_available}")   # False during maintenance
print(f"Ready to process : {can_process}")   # True if not busy
