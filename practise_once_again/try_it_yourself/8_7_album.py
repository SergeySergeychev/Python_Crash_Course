# Write a func. called make_album() that builds dictionary.
# Function should take in an artist name and an album title.
# Return a dictionary container of an artists name and albums title.
# Print return value, check if it's stored correctly
# Add an optional parameter number_of_tracks to make_album()
# If the calling line includes a value for the number of tracks,
# add that value to the dictionary/

def make_album(artist_name, album_title, number_of_tracks=''):
    """Simple attempt to represent album"""
    album = {'artist': artist_name.title(), 'album': album_title.title()}
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album

jimi = make_album('jimi', 'go go go', 6)
alsu = make_album('alsu', 'sneg', 8)
decl = make_album('decl', 'vecherinka')

albums = [jimi, alsu, decl]
for album in albums:
    print(album)
