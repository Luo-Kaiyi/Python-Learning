def make_album(singer, album, number=''):
    album = {'singer_name': singer.title(), 'album_name': album.title()}
    if number != '':
        album['songs number'] = int(number)
    return album


singer = input("请输入歌手名（输入为'quit'时结束）:\n")
album = input("请输入专辑名（输入为'quit'时结束）:\n")
while singer != 'quit' and album != 'quit':
    print(make_album(singer,album))
    singer = input("请输入歌手名（输入为'quit'时结束）:\n")
    album = input("请输入专辑名（输入为'quit'时结束）:\n")