from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
def example():
    name, num_of_lab, group, num_of_course = 'Полина Топорнина', 2, 'ФБИ-12', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    books = [
        {'author': 'Гудман Уитни', 'name': 'Токсичный позитив', 'genre': 'Психология', 'pages': '288'},
        {'author': 'Зеланд Вадим', 'name': 'Шелест утренних звезд', 'genre': 'Психология', 'pages': '224'},
        {'author': 'Ючжон Чон', 'name': 'Семилетняя ночь', 'genre': 'Ужасы', 'pages': '640'},
        {'author': 'Кинг Стивен', 'name': 'Все предельно', 'genre': 'Ужасы', 'pages': '512'},
        {'author': 'Дуксин Андрей', 'name': 'SCP Foundation. Secure. Contain. Protect. Красный том', 'genre': 'Фэнтези', 'pages': '288'},
        {'author': 'Джордж Клейсон', 'name': 'Самый богатый человек в Вавилоне', 'genre': 'Деловая литература', 'pages': '224'},
        {'author': 'Скотт Эмма', 'name': 'Среди тысячи слов', 'genre': 'Любовный роман', 'pages': '544'},
        {'author': 'Стрелеки Джон', 'name': 'Возвращение в кафе', 'genre': 'Психология', 'pages': '320'},
        {'author': 'Цысинь Лю', 'name': 'Темный лес', 'genre': 'Фантастика', 'pages': '640'},
        {'author': 'Кенилли Томас', 'name': 'Список Шиндлера', 'genre': 'Реализм', 'pages': '480'}
    ]
    return render_template('example.html',
                           name=name, lab=num_of_lab, group=group, 
                           course=num_of_course, fruits=fruits, books=books)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/dobermans')
def dobermans():
    return render_template('dobermans.html')
