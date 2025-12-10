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
print(f"Account is active: {account_active}")

if __name__ == "__main__":
    print("\nUser Authentication Demo Completed!")

# IN CASE I FORGOT WHAT HAPPENED AI EXPLANATION:
"""
def print_section(title):
    # Prints a formatted title separator for better readability
    print(f"\n{'=' * 70}")
    print(f"{title}")       # fixed bug: now prints the actual title variable
    print(f"\n{'=' * 70}")


print_section("user authentication system".title())

# --- Initial states for authentication ---
has_valid_password = True      # User entered a correct password
account_status = True          # User account is active
is_admin = False               # User does NOT have admin privileges

print("Initial Security States:")
print(f"Valid password provided: {has_valid_password}")
print(f"Account is active: {account_status}")
print(f"Has admin privileges: {is_admin}\n")

print("Performing authentication checks...\n")

# User can log in only if both password and account status are valid
can_login = has_valid_password and account_status
print(f"Can user log in to the system? {can_login}")

print("\nChecking administrative access...\n")

# Admin panel requires both login AND admin rights
can_access_admin = can_login and is_admin
print(f"Can access admin panel? {can_access_admin}")

print("\nSimulating account deactivation...")

# --- Update state: the account becomes inactive ---
account_active = False

# Recalculate login + admin status after deactivation
can_login = has_valid_password and account_active
can_access_admin = can_login and is_admin

print("\nUpdated Security States:")
print(f"Account is active: {account_active}")


# --- PROGRAM EXECUTION ENTRY POINT ---
if __name__ == "__main__":
    # This block only runs when the file is executed directly,
    # not when imported as a module in another script.
    print("\nUser Authentication Demo Completed!")
"""