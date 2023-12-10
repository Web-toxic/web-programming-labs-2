from flask import Flask
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, Blueprint, redirect, session
import psycopg2
from Db import db
# Данные объекты представляют из себя таблицы users и articles в БД

from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

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
def  l_articles():
    my_articles = articles.query.filter_by(user_id=int(current_user.id)).all()
    print(my_articles[0])
    return render_template("list_articles.html", articles=my_articles)


@lab6.route("/lab6/new_article_6", methods=['GET', 'POST'])
@login_required
def createArticle():
    errors = ""
    userID = session.get('id')

    if request.method=='GET':
        return render_template('new_article_6.html')
    else:
        userID = current_user.id
        text_article = request.form.get("text_article")
        title = request.form.get("title")

        if len(text_article) == 0:
            errors = "Заполните текст"
            return render_template('new_article_6.html', errors=errors)
        else:
            is_public = request.form.get('is_publish')
            if is_public == 'False':
                is_public = None
            else:
                is_public = True
            new_article = articles(user_id = userID, title = title, article_text=text_article, is_public=is_public)

    db.session.add(new_article)
    db.session.commit()

    return redirect(f"/lab6/list_articles")


@lab6.route("/lab6/list_articles")
@login_required
def listArticles():
    username = users.query.filter_by(id=current_user.id).first().username
    list_articles = articles.query.filter_by(user_id=current_user.id).all()

    return render_template("list_articles.html", username=username,  list_articles= list_articles)


@lab6.route("/lab6/articles/<int:article_id>")
@login_required
def getArticle(article_id):
    username = users.query.filter_by(id=current_user.id).first().username
    title = articles.query.filter_by(id=article_id).first().title
    text = articles.query.filter_by(id=article_id).first().article_text
    return render_template("articleN_6.html", title=title, article_text=text, username=username)


@lab6.route("/lab6/article_publish_list", methods = ['GET', 'POST'])
@login_required
def published():
    username = users.query.filter_by(id=current_user.id).first().username
    if articles.query.filter_by(is_public=True).all() is None:
        list = 'Нет опубликованных статей'
        return render_template("publish_article_6.html", article_published_list=list, username = username)
    else:
        list = articles.query.filter_by(is_public=True).all()
        return render_template("publish_article_6.html", article_published_list=list, username = username)
    

@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6/login")