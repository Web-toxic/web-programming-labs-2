# импортируем переменную db из файла_init.py__

from . import db
from flask_login import UserMixin

'''
Описываем схему нашей БД в виде объектов
Таким образом, создание таблиц (схемы БД) возьмет
на себя SQLAlchemy - система ORM.
'''

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(102), nullable=False)

class articles (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(50), nullable=False)
    article_text = db.Column(db.Text, nullable=False)
    is_favorite = db.Column(db.Boolean)
    is_public = db.Column(db.Boolean)
    likes = db.Column(db.Integer)