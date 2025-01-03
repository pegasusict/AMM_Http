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
__version__ = "0.0.0"
__build_date__ = 20250103

from AMM_HTTP.Models import File, Track


def api_detail(model: str, command: str, item_id: int):
    if model.lower() not in ["file", "person", "album", "track", "label", "genre", "key"]:
        return 404
    if command.lower() not in ["view", "edit"]: return 404


def api_list(model: str, filters: list = None, results: list = None):
    if model.lower() not in ["file", "person", "album", "track", "label", "genre", "key"]:
        return 404
    if not filters:
        match model.lower():
            case "file":
                return File.get_all()
            case "track":
                return Track.get_all()
