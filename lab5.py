from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, Blueprint, redirect, session
import psycopg2

lab5 = Blueprint('lab5',__name__)

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
    
    if not (username or password):
        errors = "Пожалуйтса, заполните все поля"
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
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect('/lab5')
    else:
        errors = "Неправильный логин или пароль"
        return render_template("login5lab.html", errors=errors)