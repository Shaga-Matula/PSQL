from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Executing the instructions from out "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create a Var for "Artist" table
artist_table = Table(
    "Artist", meta,
)


# make connection
with db.connect() as connection:
