def make_shirt(size='large', message='I love Python'):
    """Display the size and message of a shirt."""
    print(f"The shirt is size {size} and says '{message}'.")


make_shirt()
make_shirt('medium')
make_shirt('small', 'Hello, world!')


def make_album(artist, title, songs=None):
    """Return a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


print(make_album('Adele', '21'))
print(make_album('Queen', 'A Night at the Opera', songs=12))

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


my_profile = build_profile(
    'sinta', 'wulandari',
    location='central java',
    hobby='cycling',
)
print(my_profile)