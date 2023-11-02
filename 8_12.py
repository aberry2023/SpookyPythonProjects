def make_sandwiches(*items):
    """Make a sandwich with the given items."""
    print("\nIll make you a great sandwich:")
    for item in items:
        print(" ...adding " + item + "to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast', 'provolone', 'lettuce')
make_sandwich('turkey', 'tomatoes', 'eggs')
make_sandwich('ham', 'pickles', 'mayo')
