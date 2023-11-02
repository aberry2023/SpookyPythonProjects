def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict -= {
        'artist': artist.title(),
        'title': title.title(),
         }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('megadeth', 'countdown to extinction')
print(album)

album = make_album('lil uzi', 'lil uzi vert vs. the world')
print(album)

album = make_album('oliver francis', 'bape music')
print(album)

album = make_album('J.Cole', 'Born Sinner')
print(album)

