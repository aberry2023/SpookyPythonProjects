def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

magicians = ['harry houdini', 'Criss angel', 'David Copperfield']
show_magicians(magicians)