def print_section(title):
    print(f"\n{'=' * 70}")
    print(f"title")
    print(f"\n{'=' * 70}")

print_section("user authentication system".title())
has_valid_password = True
account_status = True
is_admin = False

print("Initial Security States:")
print(f"Valid password provided: {has_valid_password}")
print(f"Account is active: {account_status}")
print(f"has admin privileges: {is_admin}")
print("\nPerforming authentication checks...\n")

can_login = has_valid_password and account_status
print(f"Can user log in to the system? {can_login}")
print("\nChecking administative access...\n")
can_access_admin = can_login and is_admin
print(f"Can access admin panel? {can_access_admin}")
print("\nSimulating account deactivation...")
account_active = False
can_login = has_valid_password and account_active
can_access_admin = can_login and is_admin
print("\nupdated security states:".title())
print(f"account is active: {account_active}")

