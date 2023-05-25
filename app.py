import os
from flask import Flask,request, render_template, redirect, url_for

from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
#-------------------- Generic Routes --------------------------------

@app.route('/', methods=['GET'])
def show_homepage():
    return render_template("index.html")

# ------------------- albums routes --------------------------------


@app.route('/albums', methods=['GET'])
def list_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('music_pages/albums.html', albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def get_album_by_ID(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    albums = repository.find(id)
    artist = artist_repository.find(albums.artist_id)
    return render_template('music_pages/find.html', albums=albums, artist=artist)

@app.route('/albums', methods=['POST'])
def add_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    title = request.form['title']
    release_year = int(request.form['release_year'])
    artist_name = request.form['artist_name']
    album = Album(None, title, release_year, artist_name)
    new_album = repository.create(album)

    return redirect(f"albums/{new_album.id}")


@app.route('/albums/new', methods=['GET'])
def create_a_new_album():
    return render_template('music_pages/new_album.html')



# ------------------- Artists routes --------------------

@app.route('/artists', methods=['GET'])
def list_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('music_pages/artists.html', artists=artists)

# @app.route('/add', methods=['POST'])
# def add_artist():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artist = Artist( None, request.form["name"], request.form["genre"])
#     artist = repository.create(artist)
#     return "Artist added successfully"

@app.route('/artists/<int:id>',  methods=['GET'])
def get_artist_by_id(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template("music_pages/get_artist.html", artist=artist)

@app.route('/artists', methods=['POST'])
def add_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist_name = request.form["artist_name"]
    artist_genre = request.form["genre"]
    artist = Artist(None, artist_name, artist_genre)
    artist_id = repository.create(artist)
    return redirect(f"artists/{artist_id}")

@app.route('/artists/new', methods=['GET'])
def create_a_new_artist():
    return render_template('music_pages/new_artist.html')




# ======================= END OF ROUTES =====================

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
