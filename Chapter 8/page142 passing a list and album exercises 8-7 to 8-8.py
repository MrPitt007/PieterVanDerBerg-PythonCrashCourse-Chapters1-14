

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)



def make_album(artist_name, album_title, num_songs=None):
    """
    Build a dictionary describing a music album.
    Optional:
        num_songs → number of songs on the album
    """
    album = {
        'artist': artist_name.title(),
        'album': album_title.title()
    }
    if num_songs:
        album['songs'] = num_songs
    return album

# Exercise calls:
print(make_album('metallica', 'ride the lightning'))
print(make_album('nirvana', 'nevermind'))
print(make_album('pink floyd', 'the wall', num_songs=26))


