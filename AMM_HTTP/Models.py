# -*- coding: utf-8 -*-
#  Copyleft  2021-2025 Mattijs Snepvangers.
#  This file is part of Audiophiles' Music Manager, hereafter named AMM.
#
#  AMM is free software: you can redistribute it and/or modify  it under the terms of the
#   GNU General Public License as published by  the Free Software Foundation, either version 3
#   of the License or any later version.
#
#  AMM is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#   without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#   along with AMM.  If not, see <https://www.gnu.org/licenses/>.

__version__ = "0.2.4"
__build_date__ = 20250103

import enum
from datetime import datetime, UTC

from sqlalchemy import Enum, Integer, String, Column, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

from AMM_HTTP import db

Base = declarative_base()


class ItemBase(Base):
    """ base class for item tables """
    id = Column(Integer, primary_key=True)


class OptFieldBase(Base):
    """ base class for optional fields """
    pass


class RelationBase(Base):
    """ base class for relation tables """
    pass


#######################################################################
class Stat(ItemBase):
    __tablename__ = "Stats"
    name = Column(String, nullable=False)
    value = Column(Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"Stat {self.name}"


class StatRange(OptFieldBase):
    __tablename__ = "StatRanges"
    stat_id = Column(Integer, ForeignKey("Stats"))
    range_start = Column(Float, default=0)
    range_end = Column(Float)


#######################################################################
class Codecs(enum.Enum):
    wav = 0
    wma = 1
    mp2 = 2
    mp3 = 3
    mp4 = 4
    m4a = 5
    flac = 6


class PersonRoles(enum.Enum):
    artist = 0
    conductor = 1
    composer = 2
    lyricist = 3
    producer = 4


#######################################################################
class File(ItemBase):
    __tablename__ = "Files"
    track_id = Column(Integer, ForeignKey("Tracks"))
    audio_ip = Column(String(length=80))
    import_path = Column(String, nullable=False)
    imported = Column(DateTime, default=datetime.now(UTC))
    processed = Column(DateTime, onupdate=datetime.now(UTC))
    bit_rate = Column(Integer)
    codec = Column(Enum(Codecs))
    length = Column(Float)
    stage = Column(Integer, default=0)

    def __repr__(self) -> str:
        return f"File {self.id}"


class Track(ItemBase):
    __tablename__ = "Tracks"
    compose_date = Column(DateTime, default="1900-1-1")
    release_date = Column(DateTime, default="1900-1-1")

    def __repr__(self) -> str:
        return f"Track {self.id}"


class Album(ItemBase):
    __tablename__ = "Albums"
    discs = Column(Integer)
    tracks = Column(Integer)
    label_id = Column(Integer, ForeignKey("Labels"))
    release_date = Column(DateTime, default="1900-1-1")

    def __repr__(self) -> str:
        return f"Album {self.id}"


class Person(ItemBase):
    __tablename__ = "Persons"
    mbid = Column(String(40), unique=True)
    first_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    born = Column(DateTime)
    deceased = Column(DateTime)

    def __repr__(self) -> str:
        return f"Person {self.id}"


class Label(ItemBase):
    __tablename__ = "Labels"
    name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Label {self.id}"


class Key(ItemBase):
    __tablename__ = "Keys"
    name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Key {self.id}"


class Genre(ItemBase):
    __tablename__ = "Genres"
    name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Genre {self.id}"


#######################################################################
class FilePath(OptFieldBase):
    __tablename__ = "FilePaths"
    file_id = Column(Integer, primary_key=True)
    path = Column(String, nullable=False)
    definitive = Column(db.Bool)


class TrackMBid(OptFieldBase):
    __tablename__ = "TrackMBids"
    track_id = Column(Integer, primary_key=True)
    mbid = Column(String(40), unique=True)


class TrackLyric(OptFieldBase):
    __tablename__ = "TrackLyrics"
    track_id = Column(Integer, primary_key=True)
    Lyric = Column(String)


class TrackTitle(OptFieldBase):
    __tablename__ = "TrackTitles"
    track_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    main = Column(db.Bool, default=True, primary_key=True)


class AlbumMBid(OptFieldBase):
    __tablename__ = "AlbumMBids"
    album_id = Column(Integer, primary_key=True)
    mbid = Column(String(40), unique=True)


class AlbumTitle(OptFieldBase):
    __tablename__ = "AlbumTitles"
    album_id = Column(Integer, ForeignKey("Albums"))
    title = Column(String, nullable=False)
    main = Column(db.Bool, default=True)


class AlbumArt(OptFieldBase):
    __tablename__ = "AlbumArts"
    album_id = Column(Integer, ForeignKey("Albums"))
    art_path = Column(String)


class PersonPicture(OptFieldBase):
    __tablename__ = "PersonPictures"
    person_id = Column(Integer, ForeignKey("Persons"))
    picture_path = Column(String)


class TrackPerson(OptFieldBase):
    __tablename__ = "TrackPersons"
    track_id = Column(Integer, ForeignKey("Tracks"))
    person_id = Column(Integer, ForeignKey("Persons"))
    role = Column(Enum(PersonRoles))


class AlbumPerson(OptFieldBase):
    __tablename__ = "AlbumPersons"
    album_id = Column(Integer, ForeignKey("Albums"))
    person_id = Column(Integer, ForeignKey("Persons"))
    role = Column(Enum(PersonRoles))


#######################################################################
class LabelParent(RelationBase):
    __tablename__ = "LabelParentRelations"
    label_id = Column(Integer, ForeignKey("Labels"))
    parent_id = Column(Integer, ForeignKey("Labels"))


class LabelOwner(RelationBase):
    __tablename__ = "LabelOwnerRelations"
    label_id = Column(Integer, ForeignKey("Labels"))
    owner_id = Column(Integer, ForeignKey("Persons"))


class TrackKey(RelationBase):
    __tablename__ = "TrackKeyRelations"
    track_id = Column(Integer, ForeignKey("Tracks"))
    key_id = Column(Integer, ForeignKey("Keys"))


class GenreParent(RelationBase):
    __tablename__ = "GenreParentRelations"
    genre_id = Column(Integer, ForeignKey("Genres"))
    parent_id = Column(Integer, ForeignKey("Genres"))


class TrackGenre(RelationBase):
    __tablename__ = "TrackGenreRelations"
    track_id = Column(Integer, ForeignKey("Tracks"))
    genre_id = Column(Integer, ForeignKey("Genres"))


class AlbumGenre(RelationBase):
    __tablename__ = "AlbumGenreRelations"
    album_id = Column(Integer, ForeignKey("Albums"))
    genre_id = Column(Integer, ForeignKey("Genres"))
