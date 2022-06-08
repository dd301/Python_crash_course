def make_album(art_name, alb_name, num_tracks=''):
    album = {'artist' : art_name,
              'album' : alb_name}
    if num_tracks:
        album['number of tracks'] = num_tracks
    return album

while True:
    flag = input('\nEnter q to quit, press enter to continue: ')
    if flag == 'q':
        break
    artist = input('\nEnter the artist name: ')
    album = input('\nEnter the album name: ')
    alb = make_album(artist, album)
    print(alb)

