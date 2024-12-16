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
from logging import error

from AMM_HTTP import app
from AMM_HTTP.Models import File, Person, Album, Track, Label, Genre, Key, Stats
from flask import render_template, request, redirect

@app.route("/")
def index():  # generate dashboard
    dash_data = Stats.query.all()
    return render_template("index.html", dash_data=dash_data)


@app.route("<model>/<view>/<command>/<id>", strict_slashes=False, methods=["GET", "POST"])
@app.route("<model>/<view>/<command>", strict_slashes=False, methods=["GET", "POST"])
@app.route("<model>/<view>", strict_slashes=False, methods=["GET"])
@app.route("<model>", strict_slashes=False, methods=["GET"])
def mvc(model: str, view: str = None, command: str = None, id: str = None):
    if model.lower() not in ["file", "person", "album", "track", "label", "genre", "key"]:
        return 404
    else:
        if view.lower() is not None and view in ["list", "detail"]:
            if command.lower() is not None and command in ["search", "edit", "print"]:
                if command == "search":
                    filters =[]
                    results=[]
                    query = f"GET FROM `{model}` WHERE "
                    for k, v in request.form:
                        filters[k] = v
                        pass
                    if model == File: results = File.query(query).all
                    elif model == Person: results = Person.query(query).all
                    elif model == Album: results = Album.query(query).all
                    elif model == Track: results = Track.query(query).all
                    elif model == Label: results = Label.query(query).all
                    elif model == Genre: results = Genre.query(query).all
                    elif model == Key: results = Key.query(query).all
                    else: error("unknown model")
                    return render_template("list.html", model=model, filters=filters, results=results)
                elif command == "edit":
                    return render_template("detail.html", model=model, command="edit", id=id)
                elif command == "print":
                    return render_template("print.html", model=model, view=view, command="print", id=id)
                else:
                    return render_template("detail.html", model=model, command="view", id=id)
        else:
            return render_template("list.html", model=model)

"""
    # add a task  
    if request.method == "POST":  
        current_task = request.form["content"]  
        new_task = Track(content=current_task)  
        try:  
            db.session.add(new_task)  
            db.session.commit()  
            return redirect("/")  
        except Exception as e:  
            print(f"Error: {e}")  
            return f"Error: {e}"  
    # list all tasks  
    else:  
        tasks = MyTask.query.order_by(MyTask.created).all()  
        return render_template("index.html", tasks=tasks)
    """
