from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/music_web_app_html.sql") 
    repository = ArtistRepository(db_connection) 
    artists = repository.all() 

    assert artists == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "Rolling Stones", "Rock"),
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(1)
    assert artist == Artist(1, "Pixies", "Rock")


"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "The Beatles", "Rock"))

    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "Rolling Stones", "Rock"),
        Artist(3, "The Beatles", "Rock")
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = ArtistRepository(db_connection)
    repository.delete(3) 

    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "Rolling Stones", "Rock")
    ]
