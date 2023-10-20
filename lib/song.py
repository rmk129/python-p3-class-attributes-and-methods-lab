class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, gen):
        if gen in cls.genres:
            pass
        else:
            cls.genres.append(gen)

    @classmethod
    def add_to_artists(cls, art):
        if art in cls.artists:
            pass
        else:
            cls.artists.append(art)

    @classmethod
    def add_to_genre_count(cls, gen):
        if gen in cls.genres:
            cls.genre_count[gen] += 1
        else:
            cls.genre_count[gen] = 1

    @classmethod
    def add_to_artist_count(cls, art):
        if art in cls.artists:
            cls.artist_count[art] += 1
        else:
            cls.artist_count[art] = 1


    