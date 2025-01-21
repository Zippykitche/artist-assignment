from flask import Flask, make_response, jsonify
import os
from flask_migrate import Migrate
from models import db, Artist, Album

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), "chinook.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

#get all artists
@app.route('/artists', methods=['GET'])
def get_all_artists():
    artists = Artist.query.all()
    return make_response(jsonify([artist.to_dict() for artist in artists]), 200)

# Get artist by id
@app.route('/artists/<int:id>')
def artist_by_id(id):
    artist = Artist.query.filter(Artist.artistId == id).first()

    if artist:
        body = artist.to_dict()
        status = 200
    else:
        body = {'message': f'Artist {id} not found.'}
        status = 404

    return make_response(body, status)

# Get all albums by a specific artist
@app.route('/artists/<int:id>/albums', methods=['GET'])
def get_all_albums_by_artist(id):
    albums = Album.query.filter(Album.artistId == id).all()

    if albums:
        body = [album.to_dict() for album in albums]  
        status = 200
    else:
        body = {'message': f'No albums found for artist {id}.'}
        status = 404

    return make_response(body, status)

# Get all albums
@app.route('/albums', methods=['GET'])
def get_all_albums():
    albums = Album.query.all() 

    if albums:
        body = [album.to_dict() for album in albums]  
        status = 200
    else:
        body = {'message': 'No albums found.'}
        status = 404

    return make_response(body, status)


# Get the artist(s) for a specific album
@app.route('/albums/<int:id>/artist', methods=['GET'])
def get_artist_by_album(id):
    artist = Album.query.filter(Album.artistId == id).first()
    
    if artist:
        body = [artist.to_dict() for artist in artist]  
        status = 200
    else:
        body = {'message': f'No artists found for album {id}.'}
        status = 404

    return make_response(body, status)

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
