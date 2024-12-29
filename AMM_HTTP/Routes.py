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
__version__ = "0.1.1"
__build_date__ = 20241229

from logging import error

from flask import render_template, request

from AMM_HTTP import app
from AMM_HTTP.Models import File, Person, Album, Track, Label, Genre, Key, Stat


@app.route("/")
def index():  # generate dashboard
    dash_data = Stat.query.all()
    return render_template("dashboard.html", dash_data=dash_data)


@app.route("<model>/<view>/<command>/<id_number>/", strict_slashes=False, methods=["GET", "POST"])
@app.route("<model>/<view>/create/", strict_slashes=False, methods=["GET", "POST"])
@app.route("<model>/<view>/", strict_slashes=False, methods=["GET"])
@app.route("<model>/", strict_slashes=False, methods=["GET"])
def mvc(model: str, view: str = None, command: str = None, id_number: int = None):
    if model.lower() not in ["file", "person", "album", "track", "label", "genre", "key"]:
        return 404
    else:
        if view.lower() is not None and view in ["list", "detail"]:
            if command.lower() is not None and command in ["search", "edit", "print", "view"]:
                if command == "search":
                    filters = []
                    results = []
                    first_processed = False
                    query = f"GET FROM `{model}` WHERE "
                    for k, v in request.form["filters"]:
                        filters[k] = v
                        if not first_processed:
                            query += f"{k} LIKE {v} "
                            first_processed = True
                        else:
                            query += f"AND {k} LIKE {v} "
                    if model == File:
                        results = File.query(query).all
                    elif model == Person:
                        results = Person.query(query).all
                    elif model == Album:
                        results = Album.query(query).all
                    elif model == Track:
                        results = Track.query(query).all
                    elif model == Label:
                        results = Label.query(query).all
                    elif model == Genre:
                        results = Genre.query(query).all
                    elif model == Key:
                        results = Key.query(query).all
                    else:
                        error("unknown model")
                    return render_template("list.html", model=model, filters=filters, results=results)
                elif command == "edit":
                    return render_template("detail.html", model=model, command="edit", id_number=id_number)
                elif command == "print":
                    return render_template("print.html", model=model, view=view, command="print", id_number=id_number)
                else:
                    return render_template("detail.html", model=model, command="view", id_number=id_number)
        else:
            return render_template("list.html", model=model)
