from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, Blueprint, render_template, redirect, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy

RGZ=Blueprint('RGZ',__name__)

RGZ.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/my_database'
db = SQLAlchemy(RGZ)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))


@RGZ.route('/RGZ/')
def main():
    return render_template('RGZ/messenger.html')


# Функция для авторизации пользователя
def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return user
    return None

# Функция для регистрации пользователя
def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return False
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return True

# Функция для получения списка всех пользователей
def get_users():
    return User.query.all()

# Функция для отправки сообщения
def send_message(sender_id, receiver_id, message):
    message_model = Message(sender_id=sender_id, receiver_id=receiver_id, message=message)
    db.session.add(message_model)
    db.session.commit()

# Функция для получения сообщений для конкретного пользователя
def get_messages(user_id):
    return Message.query.filter_by(receiver_id=user_id).all()

# Функция для удаления сообщения
def delete_message(message_id):
    message_model = Message.query.filter_by(id=message_id).first()
    db.session.delete(message_model)
    db.session.commit()

# Маршруты
@RGZ.route('/')
def index():
    if request.user:
        return redirect('/messages')
    return render_template('index.html')

@RGZ.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login_user(username, password)
        if user:
            request.user = user
            return redirect('/messages')
        return render_template('login.html', error='Неверный логин или пароль')
    return render_template('login.html')

@RGZ.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register_user(username, password):
            return redirect('/login')
        return render_template('register.html', error='Пользователь с таким именем уже существует')
    return render_template('register.html')

@RGZ.route('/messages')
def messages():
    if not request.user:
        return redirect('/')
    users = get_users()
    messages = get_messages(request.user.id)
    return render_template('messages.html', users=users, messages=messages)

@RGZ.route('/send_message', methods=['POST'])
def send_message():
    if not request.user:
        return redirect('/')
    receiver_id = int(request.form['receiver_id'])
    message = request.form['message']
    send_message(request.user.id, receiver_id, message)
    return redirect('/messages')

@RGZ.route('/delete_message/<int:message_id>', methods=['POST'])
def delete_message(message_id):
    if not request.user:
        return redirect('/')


@RGZ.app_errorhandler(404)
def not_found(err):
    return render_template('lab9/404.html'), 404


@RGZ.app_errorhandler(500)
def server_error(err):
    return render_template('lab9/500.html'), 500


@RGZ.route('/lab9/500')
def server_error():
    return render_template('lab9/500.html')

