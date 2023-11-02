class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

Pizza_Planet = Restaurant('Pizza Planet', 'pizza')
Pizza_Planet.describe_restaurant()

Barrios = Restaurant("Barrios", 'italian')
Barrios.describe_restaurant()

rose_garden = Restaurant('rose garden', 'chinese food')
rose_garden.describe_restaurant()