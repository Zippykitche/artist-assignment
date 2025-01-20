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

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    release_date = db.Column(db.Date)  # Add release date field

    artist = db.relationship('Artist', backref='albums')

    def __repr__(self):
        return f'<Album {self.id}, {self.title}, {self.artist_id}>'

class Artist(db.Model, SerializerMixin):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Artist {self.id}, {self.name}>'
