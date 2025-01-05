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
from Models import File, FilePath,Track,Title,MBid,Codecs

__version__ = "0.0.0"
__build_date__ = 20250105


### FILE

# File.import_path
# File.bit_rate
# File.length
# File.imported
# File.processed
# File.stage
# Codecs.codec
# FilePath.quarantine_path (opt)
# FilePath.definitive_path (opt)
# Track.compose_date
# Track.release_date
# TrackTitle.title
# TrackTitle.subtitle
# TrackLyric.lyric
# Person.performer (opt plural)
# Person.composer (opt plural)
# Person.lyricist (opt plural)
# Person.producer (opt plural)
# Genre.genre (opt plural)
# Key.key
## AlbumTitle.title    #
## Person.album_artist #        sets sorted by release_date, ascending
## Album.release_date  #

def get_file_info(file_id:int):
    file_info = File.get_or_404(file_id)
    return file_info
