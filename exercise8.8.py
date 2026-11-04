def make_album(artist, judul, lagu=None):
    album = {'artis': artist, 'judul': judul}
    if lagu:
        album['Lagu'] = lagu
    return album

while True:
    print("\nTolong berikan detail album")

    artist = input("Nama Artis: ")
    if artist == 'quit':
        break

    judul = input("Judul album: ")
    if judul == 'quit':
        break

    album = make_album(artist, judul)
    print(album)
