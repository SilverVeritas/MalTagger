from collections import OrderedDict
class Song:
    # Get Opening
    def get_opening(self, soup):
        music_indexes = None
        music_songs = None
        music_artists = None

        songs_with_missing = None
        songs_with_link = None

        music = soup.find(class_="theme-songs js-theme-songs opnening")

        music_artists = [a.text.strip()[3:] for a in music.find_all(class_="theme-song-artist")]

        music_indexes = [int(idx.text.strip().strip(':')) for idx in music.find_all(class_="theme-song-index")]
        if not music_indexes:
            music_indexes = [num+1 for num in range(len(music_artists))]
            

        songs_with_missing = [song.previous.strip() for song in music.find_all(class_="theme-song-artist")]
        songs_with_link = [idx.text.strip() for idx in music.find_all(class_="theme-song-title")]

        music_artists = [a.text.strip()[3:] for a in music.find_all(class_="theme-song-artist")]

        if not songs_with_missing:
            music_songs = [song.strip().strip('"') for song in songs_with_link]
        else:
            for i in range(len(songs_with_missing)):
                if songs_with_missing[i] == '':
                    songs_with_missing[i] = songs_with_link.pop(0)

            music_songs = [song.strip('"') for song in songs_with_missing]

        dic = OrderedDict()
        for x in music_indexes:
            idx = music_indexes.index(x)
            dic[x] = [music_songs[idx], music_artists[idx]]
        sorted_songs = dict(sorted(dic.items()))

        self.songlist_op = []
        for k in sorted_songs.keys():
            # songlist_op.append([sorted_songs[k][0], sorted_songs[k][1], k])
            self.songlist_op.append({
                'song' : sorted_songs[k][0],
                'artist' : sorted_songs[k][1],
                'index' : int(k)
            })
        # /Get Opening


    def get_openings(self, soup):
        music_indexes = None
        music_songs = None
        music_artists = None

        songs_with_missing = None
        songs_with_link = None

        music = soup.find(class_="theme-songs js-theme-songs opnening")

        music_artists = [a.text.strip()[3:] for a in music.find_all(class_="theme-song-artist")]

        music_indexes = [int(idx.text.strip().strip(':')) for idx in music.find_all(class_="theme-song-index")]
        if not music_indexes:
            music_indexes = [num+1 for num in range(len(music_artists))]
            

        songs_with_missing = [song.previous.strip() for song in music.find_all(class_="theme-song-artist")]
        songs_with_link = [idx.text.strip() for idx in music.find_all(class_="theme-song-title")]

        music_artists = [a.text.strip()[3:] for a in music.find_all(class_="theme-song-artist")]

        if not songs_with_missing:
            music_songs = [song.strip().strip('"') for song in songs_with_link]
        else:
            for i in range(len(songs_with_missing)):
                if songs_with_missing[i] == '':
                    songs_with_missing[i] = songs_with_link.pop(0)

            music_songs = [song.strip('"') for song in songs_with_missing]

        dic = OrderedDict()
        for x in music_indexes:
            idx = music_indexes.index(x)
            dic[x] = [music_songs[idx], music_artists[idx]]
        sorted_songs = dict(sorted(dic.items()))

        self.songlist_op = []
        for k in sorted_songs.keys():
            # songlist_op.append([sorted_songs[k][0], sorted_songs[k][1], k])
            self.songlist_op.append({
                'song' : sorted_songs[k][0],
                'artist' : sorted_songs[k][1],
                'index' : int(k)
            })
        # /Get Opening

        # Get Ending
    def get_endings(self, soup):
        music_indexes = None
        music_songs = None
        music_artists = None

        songs_with_missing = None
        songs_with_link = None

        music = soup.find(class_="theme-songs js-theme-songs ending")

        music_artists = [a.text.strip()[3:] for a in music.find_all(class_="theme-song-artist")]

        music_indexes = [int(idx.text.strip().strip(':')) for idx in music.find_all(class_="theme-song-index")]
        if not music_indexes:
            music_indexes = [num+1 for num in range(len(music_artists))]
            

        songs_with_missing = [song.previous.strip() for song in music.find_all(class_="theme-song-artist")]
        songs_with_link = [idx.text.strip() for idx in music.find_all(class_="theme-song-title")]

        music_artists = [a.text.strip()[3:] for a in music.find_all(class_="theme-song-artist")]

        if not songs_with_missing:
            music_songs = [song.strip().strip('"') for song in songs_with_link]
        else:
            for i in range(len(songs_with_missing)):
                if songs_with_missing[i] == '':
                    songs_with_missing[i] = songs_with_link.pop(0)

            music_songs = [song.strip('"') for song in songs_with_missing]

        dic = OrderedDict()
        for x in music_indexes:
            idx = music_indexes.index(x)
            dic[x] = [music_songs[idx], music_artists[idx]]
        sorted_songs = dict(sorted(dic.items()))

        self.songlist_ed = []
        for k in sorted_songs.keys():
            # songlist_op.append([sorted_songs[k][0], sorted_songs[k][1], k])
            self.songlist_ed.append({
                'song' : sorted_songs[k][0],
                'artist' : sorted_songs[k][1],
                'index' : int(k)
            })
        # /Get Ending