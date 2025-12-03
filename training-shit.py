# =========================================
# REAL LIFE USER SESSION APP
# =========================================

class UserSession:
    def __init__(self):
        # Boolean session states
        self.is_active = False
        self.ios_authenticated = False
        self.has_privileges = False

    def activate(self):
        self.is_active = True
        print("Session activated.")

    def deactivate(self):
        self.is_active = False
        self.ios_authenticated = False
        self.has_privileges = False
        print("Session deactivated.")

    def authenticate(self):
        if not self.is_active:
            print("Error: Cannot authenticate. Session is not active.")
            return
        self.ios_authenticated = True
        print("User authenticated successfully.")

    def grant_privileges(self):
        if not self.is_active or not self.ios_authenticated:
            print("Error: Cannot grant privileges. User must be authenticated first.")
            return
        self.has_privileges = True
        print("Privileges granted.")

    def validate_session(self):
        """Return True only if all conditions are met."""
        return (
            self.is_active
            and self.ios_authenticated
            and self.has_privileges
        )

    def session_status(self):
        """Print status of the session."""
        print("\n--- SESSION STATUS ---")
        print(f"Active:          {self.is_active}")
        print(f"Authenticated:   {self.ios_authenticated}")
        print(f"Has Privileges:  {self.has_privileges}")
        print(f"Valid Session:   {self.validate_session()}")
        print("-----------------------\n")


# =========================================
# MAIN APP LOOP
# =========================================

def run_app():
    session = UserSession()

    while True:
        print("Choose an action:")
        print("1. Activate Session")
        print("2. Authenticate User")
        print("3. Grant Privileges")
        print("4. Show Session Status")
        print("5. Deactivate Session")
        print("0. Exit App")

        choice = input("Enter number: ")

        if choice == "1":
            session.activate()
        elif choice == "2":
            session.authenticate()
        elif choice == "3":
            session.grant_privileges()
        elif choice == "4":
            session.session_status()
        elif choice == "5":
            session.deactivate()
        elif choice == "0":
            print("Closing app...")
            break
        else:
            print("Invalid choice. Try again.")

        print()  # Empty line for readability


# Run the app
run_app()
