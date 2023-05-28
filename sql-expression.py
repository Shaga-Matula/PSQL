from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Executing the instructions from out "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create a Var for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=(True)),
    Column("Name", String)
)

album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=(True)),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey(artist_table.ArtistId))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=(True)),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey(album_table.TrackId)),
    Column("MediaTypeId", Integer, primary_key=(False)),
    Column("GenreId", Integer, primary_key=(False)),
    Column("Composer", String),
    Column("Milliseconds", Int),
    Column("Bytes", String),
    Column("Unit Price", Float),

    
    

)

# make connection
with db.connect() as connection:
