class User():
 """Represent a simple user profile."""

 def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

 def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

 def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

antonio = User('antonio', 'berry', 'a_berry', 'a_berry@example.com', 'alaska')
antonio.describe_user()
antonio.greet_user()

rodeo = User('rodeo', 'burger', 'rodeoburger', 'rb@example.com', 'alaska')
rodeo.describe_user()
rodeo.greet_user()