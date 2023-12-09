from flask import Flask
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, Blueprint, redirect, session
import psycopg2
from Db import db
# Данные объекты представляют из себя таблицы users и articles в БД

from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6 = Blueprint('lab6',__name__)

@lab6.route('/lab6/')
def mainpage():
    try:
        username = (users.query.filter_by(id=current_user.id).first()).username
        return render_template("lab6.html", username=username)
    except:
        return render_template("lab6.html", username="Anon")


@lab6.route('/lab6/check')
def check():  
    my_users = users.query.all()
    print(my_users)
    return "result in console!"


@lab6.route('/lab6/checkarticles')
def checkarticles():
    all_articles = articles.query.all()
    print(all_articles)
    return "result in console!"


@lab6.route("/lab6/register", methods=['GET', 'POST'])
def register():
    errors = []
    if request.method == "GET":
        return render_template("register_6.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    isUserExist = users.query.filter_by(username=username_form).first()
    if username_form == '':
        errors = 'Пустое имя!'
        return render_template("register_6.html", errors=errors)
    else:
        if isUserExist is not None:
            errors = 'Такой пользователь уже существует!'
            return render_template("register_6.html", errors=errors)
        else:
            if len(password_form) < 5:
                errors = 'Пароль должен быть длиннее 5 символов!'
                return render_template("register_6.html", errors=errors)
            else:
                hashedPswd = generate_password_hash(password_form, method="pbkdf2")
                newUser = users(username=username_form, password=hashedPswd)

                db.session.add(newUser)
                db.session.commit()

    return redirect("/lab6/login")


@lab6.route("/lab6/login", methods = ['GET', 'POST'])
def login():
    errors = ''
    if request.method == "GET":
        return render_template("login_6.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    my_user = users.query.filter_by(username=username_form).first()
    if username_form is None and password_form is None:
        errors = 'Заполните все поля!'
        return render_template("login_6.html", errors=errors)
    else:
        if my_user is not None:
            if check_password_hash(my_user.password, password_form):
                login_user(my_user, remember=False)
                return redirect("/lab6")
            else:
                errors = 'Неверный пароль!'
                return render_template("login_6.html", errors=errors)
        else:
            errors = 'Пользвателя с таким именем не существует!'
            return render_template("login_6.html", errors=errors)


@lab6.route("/lab6/articles")
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=int(current_user.id)).all()
    print(my_articles[0])
    return render_template("list_articles.html", articles_list=my_articles)