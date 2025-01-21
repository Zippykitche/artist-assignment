from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import ForeignKey

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Album(db.Model, SerializerMixin):
    __tablename__ = 'albums'

    albumId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artistId = db.Column(db.Integer, db.ForeignKey('artists.artistId'))
    release_date = db.Column(db.Date)  # Add release date field

    artist = db.relationship('Artist', backref='albums')

    def __repr__(self):
        return f'<Album {self.albumId}, {self.title}, {self.artistId}, {self.release_date}>'
    
    serialize_only = ('albumId', 'title', 'artistId', 'release_date')

class Artist(db.Model, SerializerMixin):
    __tablename__ = 'artists'

    artistId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Artist {self.artistId}, {self.name}>'
    
    serialize_only = ('artistId', 'name')
