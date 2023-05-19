import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')


@app.route('/list', methods=['GET'])
def list_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

@app.route('/find/<int:id>', methods=['GET'])
def get_album_by_ID(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    artist_repository = ArtistRepository(connection)
    albums = repository.find(id)
    artist = artist_repository.find(albums.artist_id)
    return render_template('albums/find.html', albums=albums, artist=artist)

@app.route('/albums', methods=['POST'])
def add_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album( None, request.form["title"], request.form["release_year"], request.form["artist_id"])
    album = repository.create(album)
    return "Album added successfully"

@app.route('/artists', methods=['GET'])
def list_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join([
            str(artist) for artist in repository.all()
        ])

@app.route('/add', methods=['POST'])
def add_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist( None, request.form["name"], request.form["genre"])
    artist = repository.create(artist)
    return "Artist added successfully"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
