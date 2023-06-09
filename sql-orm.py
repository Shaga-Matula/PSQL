from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create class based model of the Artist table
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key = True)
    Name = Column(String)


# create class based model of the Artist table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key = True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create class based model of the Track table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumID = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column (Integer, primary_key = False)
    GenreId = Column (Integer, primary_key = False)
    Composer = Column (String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)



# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId,artist.Name, sep = " |--- ")

# Query 3
# artist = session.query(Artist).filter_by(ArtistId = "22").first()
# print(artist.ArtistId, artist.Name, sep = " | ")

Albums = session.query(Album).filter_by(ArtistId = "22")
for album in Albums:
    print(album.Title)