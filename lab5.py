from flask import Flask
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, Blueprint, redirect, session
import psycopg2

lab5 = Blueprint('lab5',__name__)

# app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# good = 0

def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="polina_knowledge_base",
        password="7414")    
    return conn;

def dbClose(cursor, connection):
# Закрываем курсор и соединение
# Порядок важен!
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def main():  
    visibleUser = 'Anon'
    visibleUser = session.get('username')
    return render_template('lab5.html', username=visibleUser)


@lab5.route('/lab5/users')
def users():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users")
    result = cur.fetchall()
    conn.close()
    return render_template('users.html', users=result)


@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def regPage():
    errors = ""

    if request.method == "GET":
        return render_template('register.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):
        errors = ("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)
    
    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors = ("Пользователь с данным именем уже существует")

        conn.close()
        cur.close()

        return render_template('register.html', errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hashPassword}');")
    
    conn.commit()
    conn.close()
    cur.close()

    return redirect('/lab5/register')


@lab5.route('/lab5/login', methods = ['GET', 'POST'])
def logPage():
    errors = ""

    if request.method == "GET":
        return render_template('login5lab.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')
    
    if (username == '' or password == ''):
        errors = "Пожалуйста, заполните все поля"
        return render_template("login5lab.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor() 

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}';")

    result = cur.fetchone()

    if result is None:
        errors = "Неправильный логин или пароль"
        dbClose(cur, conn)
        return render_template("login5lab.html", errors=errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        # print("--------------------", userID, username, "--------------------")
        session['id'] = userID
        session['username'] = username
        # print("--------------------", session['id'], session['username'], "--------------------")
        dbClose(cur, conn)
        return redirect('/lab5')
    else:
        errors = "Неправильный логин или пароль"
        return render_template("login5lab.html", errors=errors)


@lab5.route('/lab5/new_article', methods = ['GET', 'POST'])
def creatArticle():
    visibleUser = session.get('username')
    errors = ""

    userID = session.get('id')

    if userID is not None:
        if request.method == 'GET':
            return render_template('new_article.html', username=visibleUser)
        
        if request.method == 'POST':
            text_article = request.form.get('text_article')
            title = request.form.get('title_article')

            if len(text_article) == 0:
                errors = "Заполните текст"
                return render_template('new_article.html', errors=errors, username=visibleUser)
            
            conn = dbConnect()
            cur = conn.cursor() 

            cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")
            new_article_id = cur.fetchone()[0]
            conn.commit()
            dbClose(cur, conn)
            return redirect(f'/lab5/articles/{new_article_id}')

    return redirect('/lab5/login')


@lab5.route('/lab5/articles/<int:article_id>')
def getArticle(article_id):
    userID = session.get('id')

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()     

        cur.execute(f"SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found"
        
        text = articleBody[1].splitlines()

        return render_template('articleN.html', article_text = text, article_title=articleBody[0], username = session.get('username'))
    

@lab5.route('/lab5/user/articles', methods = ['GET', 'POST'])
def user_articles():
    userID = session.get('id')
    title = request.form.get('title_article')

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()     

        cur.execute(f"SELECT title, id FROM articles WHERE user_id = {userID}")

        articleBody = cur.fetchall()

        if articleBody is None:
            return "Not found"

        return render_template('user_articles.html', username = session.get('username'), article_title=articleBody)
    

@lab5.route('/lab5/logout', methods=['GET'])
def logout():
    session.clear()
    return 'You have been logged out'