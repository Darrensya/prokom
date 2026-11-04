tmptFav = {
    'ren' : ['waterpark', 'rumah'],
    'reksa' : ['seaworld', 'pantai', 'aquatic'],
    'adzra' : ['museum']
}

for nama, tempat in tmptFav.items() :
    print (f"{nama.title()} suka mengunjungi :")
    for tmpt in tempat:
        print (f"{tmpt}")
    print()