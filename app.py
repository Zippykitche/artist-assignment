from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Artist, Album

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chinook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

# Get artist by id
@app.route('/artists/<int:id>', methods=['GET'])
def find_artist_by_id(id):
    artist = Artist.query.get(id)
    if artist:
        response = make_response(jsonify(artist.to_dict()), 200)
    else:
        response = make_response(jsonify({"error": "Artist not found"}), 404)
    return response

# Get all albums by a specific artist
@app.route('/artists/<int:id>/albums', methods=['GET'])
def get_all_albums_by_artist(id):
    artist = Artist.query.get(id)
    if artist:
        albums = Album.query.filter_by(artist_id=id).all()
        response = make_response(jsonify([album.to_dict() for album in albums]), 200)
    else:
        response = make_response(jsonify({"error": "Artist not found"}), 404)
    return response

# Get the artist(s) for a specific album
@app.route('/albums/<int:id>/artist', methods=['GET'])
def get_artist_by_album(id):
    album = Album.query.get(id)
    if album:
        artist = album.artist
        response = make_response(jsonify(artist.to_dict()), 200)
    else:
        response = make_response(jsonify({"error": "Album not found"}), 404)
    return response

# Get the release date of an album
@app.route('/albums/<int:id>/release_date', methods=['GET'])
def get_album_release_date(id):
    album = Album.query.get(id)
    if album:
        response = make_response(jsonify({"release_date": album.release_date}), 200)
    else:
        response = make_response(jsonify({"error": "Album not found"}), 404)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
