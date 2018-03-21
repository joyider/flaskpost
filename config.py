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
# Filename: config by: andrek
# Timesamp:2018-03-20 :: 00:43 using PyCharm

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
	DEBUG = False
	TESTING = False
	DEV = False

	DATABASE_SETTINGS = {
		'username': os.getenv('DB_USERNAME', ''),
		'password': os.getenv('DB_PASSWORD', '!'),
		'hostname': os.getenv('DB_HOSTNAME', ''),
		'port': os.getenv('DB_PORT', '')
	}

	SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://{username}:{password}@{hostname}:{port}/Project?driver=ODBC+Driver+13+for+SQL+Server?charset'.format(
		**DATABASE_SETTINGS)
	SECRET_KEY = os.getenv('SECRET_KEY') or 'Al0ngPa@@w0rd'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	LOG_TO_STDOUT = os.getenv('LOG_TO_STDOUT')
	POSTS_PER_PAGE = 25

class TestConfig(BaseConfig):
	DEBUG = False
	TESTING = True
	DEV = False

	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))


class ProductionConfig(BaseConfig):
	DEBUG = False
	TESTING = False
	DEV = False


class DevelopmentConfig(BaseConfig):
	DEBUG = True
	TESTING = False
	DEV = True

	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
