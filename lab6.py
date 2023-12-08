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

@lab6.route("/lab6")
def mainpage():
    try:
        username = users.query.filter_by(id=current_user.id).first().username
        return render_template("lab6.html", username = username)
    except:
         return render_template("lab6.html", username = "Anon")


@lab6.route('/lab6/check')
def main():  
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