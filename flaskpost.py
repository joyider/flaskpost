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
# Filename: flaskpost by: andrek
# Timesamp:2018-03-20 :: 00:57 using PyCharm
from app import create_app, db
import argparse
from werkzeug.serving import run_simple

app = create_app()

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description="Kör Bolagsrätt API för WSGI")
	parser.add_argument('-p', '--port', help='App Port')
	parser.add_argument('-i', '--host', help='App Host')
	parser.add_argument('-r', '--reloader', action='store_true',
	                    help='Turn reloader on')
	parser.add_argument('-d', '--debug', action='store_true',
	                    help='Turn debug on')
	args = parser.parse_args()
	run_simple(
		args.host or '127.0.0.1',
		int(args.port) if args.port else 5000,
		app,
		use_reloader=args.reloader or True,
		use_debugger=args.debug or True,
		)