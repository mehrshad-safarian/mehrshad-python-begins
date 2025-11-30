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
