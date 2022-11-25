# Start with your program from ex8-7.
# Write a while loop that allows users to enter an album's artist and album_title
# Print output dictionary that's created
# Include a quit option in while loop

def make_album(artist_name, album_title):
    """Make album neatly formatted."""
    album = {
        'artist': artist_name.title(),
        'album': album_title.title()
        }
    return album

while True:
    print("\nPlease provide additional information about album")
    print(("enter 'q' at any time you want to quit"))

    artist_name = input("Hello, tell me your artist name: ")
    if artist_name == 'q':
            break

    album_title = input("Hello, tell me albums name: ")
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(album)
