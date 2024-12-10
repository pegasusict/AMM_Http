# -*- coding: utf-8 -*-
#  Copyleft  2021-2025 Mattijs Snepvangers.
#  This file is part of Pegasus-ICT Python Library, hereafter named PPL.
#
#  PPL is free software: you can redistribute it and/or modify  it under the terms of the
#   GNU General Public License as published by  the Free Software Foundation, either version 3
#   of the License or any later version.
#
#  PPL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#   without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#   along with PPL.  If not, see <https://www.gnu.org/licenses/>.
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")





if __name__ in "__main__": app.run(debug=True)
