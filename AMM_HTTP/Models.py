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

from datetime import datetime, UTC
from email.policy import default

from AMM_HTTP import db


class Stats(db.Model):
    stat_id = db.Column(db.Int, primary_key=True)
    name = db.Column(db.String, nullable=False)
    range = db.Column(db.Int, nullable=True)
    value = db.Column(db.Int, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"Stat {self.id}"


class Track(db.Model):
    id = db.Column(db.Int, primary_key=True)
    mbid = db.Column(db.String, unique=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String, nullable=True)
    key_id = db.Column(db.Int)

    def __repr__(self) -> str:
        return f"Track {self.id}"


class Album(db.Model):
    id = db.Column(db.Int, primary_key=True)
    mbid = db.Column(db.String, unique=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String, nullable=True)
    discs = db.Column(db.Int)
    tracks = db.Column(db.Int)
    label_id = db.Column(db.Int)

    def __repr__(self) -> str:
        return f"Album {self.id}"


class Person(db.Model):
    id = db.Column(db.String, primary_key=True)
    mbid = db.Column(db.String, unique=True)
    first_name = db.Column(db.String, nullable=True)
    middle_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=False)
    born = db.Column(db.DateTime)
    deceased = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f"Person {self.id}"


class File(db.Model):
    id = db.Column(db.String, primary_key=True)
    audio_ip = db.Column(db.String)
    import_path = db.Column(db.String, nullable=False)
    quarantine_path = db.Column(db.String, nullable=True)
    definitive_path = db.Column(db.String, nullable=True)
    imported = db.Column(db.DateTime, default=datetime.now(UTC))
    processed = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f"File {self.id}"


class Label(db.Model):
    id = db.Column(db.Int, primary_key=True)
    name = db.Column(db.String, nullable=False)
    parent_id = db.Column(db.Int, nullable=True)
    owner_id = db.Column(db.Int, nullable=True)

    def __repr__(self) -> str:
        return f"Label {self.id}"


class Genre(db.Model):
    id = db.Column(db.Int, primary_key=True)
    name = db.Column(db.String, nullable=False)
    parent_id = db.Column(db.Int, nullable=True)

    def __repr__(self) -> str:
        return f"Genre {self.id}"


class Key(db.Model):
    id = db.Column(db.Int, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"Key {self.id}"


class TrackPerson(db.Model):
    track_id = db.Column(db.Int, primary_key=True)
    person_id = db.Column(db.Int, primary_key=True)
    role = db.Column(db.Enum('artist', 'conductor', 'composer', 'lyricist', 'producer'))


class AlbumPerson(db.Model):
    album_id = db.Column(db.Int, primary_key=True)
    person_id = db.Column(db.Int, primary_key=True)
    role = db.Column(db.Enum('artist', 'conductor', 'composer', 'lyricist', 'producer'))


class TrackGenre(db.Model):
    track_id = db.Column(db.Int, primary_key=True)
    genre_id = db.Column(db.Int, primary_key=True)


class AlbumGenre(db.Model):
    album_id = db.Column(db.Int, primary_key=True)
    genre_id = db.Column(db.Int, primary_key=True)
