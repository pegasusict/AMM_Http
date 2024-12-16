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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL

class Stats(db.Model):
    stat_id = db.Column(db.Int, primary_key=True)
    name = db.Column(db.String, nullable=False)
    value = db.Column(db.Int, nullable=False)


class Track(db.Model):
    mbid = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String, nullable=True)
    artist_id = db.Column(db.String, nullable=False)
    composer_id = db.Column(db.String, nullable=True)
    producer_id = db.Column(db.String, nullable=True)
    registered = db.Column(db.DateTime, default=datetime.now(UTC))

    def __repr__(self) -> str:
        return f"Track {self.mbid}"

class Album(db.Model):
    mbid = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    subtitle = db.Column(db.String, nullable=True)
    artist_id = db.Column(db.String, nullable=False)
    registered = db.Column(db.DateTime, default=datetime.now(UTC))

    def __repr__(self) -> str:
        return f"Track {self.mbid}"

class Person(db.Model):
    mbid = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String, nullable=True)
    middle_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=False)
    registered = db.Column(db.DateTime, default=datetime.now(UTC))

    def __repr__(self) -> str:
        return f"Track {self.mbid}"
