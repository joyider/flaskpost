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
# Filename: routes by: andrek
# Timesamp:2018-03-20 :: 12:51 using PyCharm

from flask import render_template, redirect, url_for, request
from flask_login import login_required
from app.admin import bp

@bp.route('/')
def index():
    """Show admin overview page."""
    return render_template('index.html')


@bp.route('/new_post/')
def newpost():
    """Show admin overview page."""
    return render_template('new_post.html')
