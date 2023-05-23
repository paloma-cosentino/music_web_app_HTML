from lib.album_repository import AlbumRepository
from lib.album import Album


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/music_web_app_html.sql") 
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        ]
    
def test_create_album(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql") 
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test title", 1880, 1)
    repository.create(album)
    assert album.id == 3

    assert repository.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Test title", 1880, 1)]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(1)
    assert album == Album(1, "Doolittle", 1989, 1)