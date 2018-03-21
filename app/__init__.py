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
# Filename: __init__ by: andrek
# Timesamp:2018-03-19 :: 23:57 using PyCharm

import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from app.admin import bp as _admin_bp

db = SQLAlchemy()
lm = LoginManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask('FlaskPost')
    app.config.from_object(config_class)

    db.init_app(app)
    lm.init_app(app)

    app.register_blueprint(_admin_bp, url_prefix='/admin')

    # from app.errors import bp as errors_bp
    # app.register_blueprint(errors_bp)
    #
    # from app.auth import bp as auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')
    #
    # from app.main import bp as main_bp
    # app.register_blueprint(main_bp)
    #
    # from app.api import bp as api_bp
    # app.register_blueprint(api_bp, url_prefix='/api')

    if True:  #if not app.debug and not app.testing:

        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/flaskpost.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('FlaskPost startup')
        app.logger.info(app.url_map)

    return app
