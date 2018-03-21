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
# Filename: models by: andrek
# Timesamp:2018-03-20 :: 11:34 using PyCharm

from hashlib import md5
import datetime
from app import db
from flask_login import UserMixin

from app.utils import slugify

ROLE_USER = 0
ROLE_ADMIN = 1

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    registered = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(64))
    posts = db.relationship(
        'Post',
        order_by='Post.created.desc()',
        passive_updates=False,
        cascade='all,delete-orphan',
        backref='author',
    )
    last_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(45))
    current_login_at = db.Column(db.DateTime)
    current_login_ip = db.Column(db.String(45))

    def __init__(self, name, password):
        self.name = name
        self.change_password(password)

    def __repr__(self):
        return u'<User(%s, %s)>' % (self.id, self.name)

    def compare_password(self, password):
        """Compare password against stored password hash."""
        return check_password_hash(self.password_hash, password)

    def change_password(self, password):
        """Change current password to a new password."""
        self.password_hash = generate_password_hash(password, 6)


@lm.user_loader
def load_user(id):
    return User.query.get(id)


class Post(db.Model):
    PER_PAGE = 10

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(256), nullable=False)
    post = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False, unique=True)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False,
    )
    visible = db.Column(db.Boolean, default=False)

    def __init__(self, title, post, author_id, visible):
        self.created = datetime.utcnow()
        self.updated = self.created
        self.title = title
        self.markup = post
        self.slug = slugify(self.created, title)
        self.author_id = author_id
        self.visible = visible

    def __repr__(self):
        return u'<Post(%s,%s,%s)>' % (self.id, self.slug, self.author.name)

    def update(self, title, markup, visible):
        """Update post values.
        Handles title slug and last update tracking.
        """
        self.updated = datetime.utcnow()
        self.title = title
        self.markup = markup
        self.slug = slugify(self.created, title)
        self.visible = visible

    @property
    def is_updated(self):
        """Validate if this post has been updated since created."""
        return self.updated > self.created