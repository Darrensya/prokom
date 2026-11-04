def make_album(artist, judul, lagu=None):
    album = {'artis': artist, 'judul': judul}
    if lagu:
        album['Lagu'] = lagu
    return album


album_1 = make_album('MotherMother', 'Inside')
album_2 = make_album('The Weekend', " The Highlights")
album_3 = make_album('Billie Eilish', 'When we all fall asleep, where do we go?')


print(album_1)
print(album_2)
print(album_3)
