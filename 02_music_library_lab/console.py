import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Johny Cash")
artist_repository.save(artist1)
artist2 = Artist("Bob Marley")
artist_repository.save(artist2)

album1 = Album("Unchained", "Country", artist1)
album_repository.save(album1)
album2 = Album("Natural Mystic", "Reggae", artist2)
album_repository.save(album2)
album3 = Album("Ring of Fire", "Country", artist1)
album_repository.save(album3)
album4 = Album("Catch a Fire", "Reggae", artist2)
album_repository.save(album4)


pdb.set_trace()