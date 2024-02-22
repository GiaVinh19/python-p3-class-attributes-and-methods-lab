class Song:

    count = 0
    genres = []
    genre_count = {}
    artist_count = {}
    artists = []

    def add_song_to_count():
        Song.count += 1
    
    def add_genres(genre):
        Song.genres.append(genre)

    def add_artists(artist):
        Song.artists.append(artist)

    def add_to_genre_count(genre):
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count.update({genre : 1})

    def add_to_artist_count(artist):
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count.update({artist : 1})

    def __init__(self, name, artist, genre):
        Song.add_song_to_count()
        Song.add_genres(genre)
        Song.add_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre
        

song1 = Song("Shining", "Kota Hoshino", "experimental")
song2 = Song("Shining", "Kota Hoshino", "electric")
song3 = Song("Shining", "Kota Hoshino", "experimental")

print(Song.genre_count)