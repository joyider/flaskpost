# -*- coding: utf-8 -*-
# flaskpost(c) 2017-2018 by Andre Karlsson<andre.karlsson@protractus.se>
#
# This file is part of flaskpost.
#
#    flaskpost is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    flaskpost is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with flaskpost.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Filename: utils by: andrek
# Timesamp:2018-03-20 :: 11:45 using PyCharm

import re

from datetime import datetime

from wtforms.validators import regexp

is_name = regexp(
    # not using \w since it allows for unlimited underscores
    r'^[a-zA-Z0-9]+([ \-\_][a-zA-Z0-9]+)*$',
    message='Field characters can only be letters and digits with one space, \
            underscore or hyphen as separator.'
)


def slugify(now, str):
    """Return slug genereated from date and specified unicoded string."""
    date = datetime.date(now)
    unistr = str.lower()
    title = re.sub(r'\W+', '-', unistr).strip('-')
    return '%i/%i/%i/%s' % (date.year, date.month, date.day, title)