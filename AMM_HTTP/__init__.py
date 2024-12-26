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

from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL

app = Flask(__name__)
Scss(app)
app.AMM_DEBUG = True

db_url = URL.create(
    "mysql+pymysql",
    username="sql_master",
    password="Sql_1r3i5",  # plain (unescaped) text
    host="localhost",
    database="amm",
)
############################################################################
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////project.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True if app.AMM_DEBUG == True else False
db = SQLAlchemy(app)
