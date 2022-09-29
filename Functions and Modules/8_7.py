def make_album(artist_name, album_title, songs=None):
    """"Builds a dictionary describing a music album"""
    album = {'name': artist_name, 'title': album_title}
    
    if songs:
        album['songs'] = songs
    
    return album


print(make_album('Swae Lee', 'In the Dark'))
print(make_album('Wallows', 'Nothing Happens'))
print(make_album('Khalid', 'American Teen'))

new_album = make_album('The Weeknd', 'Starboy', 18)
print(new_album)