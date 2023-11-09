from flask import redirect, render_template, request, Blueprint
import psycopg2

lab5 = Blueprint('lab5', __name__)


@lab5.route('/lab5/')
def main():
    # Параметры подключения к БД
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "knowledge_base",
        user = "polina_knowledge_base",
        password = "7414"
    )

    # Получаем курсор. С его помощью мы можем выполнять SQL-запросы
    cur = conn.cursor()

    # Пишем запрос, который psycopg2 должен выполнить
    cur.execute("SELECT * FROM users;")

    # fetchall - получить все строки, которые получились в результате
    # выполнения SQL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()

    # Закрываем соединение с БД
    cur.close()
    conn.close()

    print(result)

    return "go to console"

@lab5.route('/lab5/users')
def users():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "knowledge_base",
        user = "polina_knowledge_base",
        password = "7414"
    )
    cur = conn.cursor()
    cur.execute("SELECT username FROM users")
    result = cur.fetchall()
    conn.close()
    return render_template('users.html', users=result)
