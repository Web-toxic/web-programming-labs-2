from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <h1>Лабораторные работы по WEB-программированию</h1>

            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа 1</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab2" target="_blank">Лабораторная работа 2</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab3" target="_blank">Лабораторная работа 3</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab4" target="_blank">Лабораторная работа 4</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/zzz" target="_blank">Защита</a>
                </li>
            </ul>
        </main>

        <footer>
            &copy; Полина Топорнина, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1/")
def lab():
    return """
<!doctype html>
<html>
    <head>
        <title>Топорнина Полина Игоревна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <a href="http://127.0.0.1:5000/menu" target="_blank">Меню</a>

        <h2>Реализованные роуты</h2>
        <ul>
            <li><a href='/lab1/oak'>/lab1/oak - дуб</a></li>
            <li><a href='/lab1/student'>/lab1/student - студент</a></li>
            <li><a href='/lab1/python'>/lab1/python - python</a></li>
            <li><a href='/lab1/raccoon'>/lab1/raccoon - енотики</a></li>
        </ul>
        
        <footer>
            &copy; Полина Топорнина, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">

        <footer>
            &copy; Полина Топорнина, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Топорнина Полина Игоревна</h1>
        <img src="''' + url_for('static', filename='logo.png') + '''">
        
        <footer>
            &copy; Полина Топорнина, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Язык программирования Python</h1>

        <p>
            <h3>Python был назван в честь комедийного шоу</h3>
            Вы могли бы подумать, что Python назван в честь змеи, но на самом деле это не так. 
            Создатель языка, Гвидо ван Россум, назвал его в честь британского комедийного шоу 
            "Летающий цирк Монти Пайтона" (Monty Python's Flying Circus), которое он любил смотреть. 
            Он также использовал названия персонажей и сцен из шоу в своих примерах кода и 
            документации. Например, он называл свои тестовые файлы "spam" и "eggs", в честь 
            знаменитого скетча о завтраке.
        </p>

        <p>
            <h3>Python имеет свою философию</h3>
            Python - не просто язык программирования, а целая философия. Его основные принципы 
            сформулированы в документе под названием "The Zen of Python", который можно прочитать, 
            набрав команду "import this" в интерпретаторе Python. Вот некоторые из них:<br>
            <ul>
                <li>Красивое лучше, чем уродливое.</li>
                <li>Явное лучше, чем неявное.</li>
                <li>Простое лучше, чем сложное.</li>
                <li>Сложное лучше, чем запутанное.</li>
                <li>Читаемость имеет значение.</li>
                <li>Ошибки никогда не должны замалчиваться.</li>
                <li>Если реализацию сложно объяснить - идея плоха.</li>
                <li>Если реализацию легко объяснить - идея, возможно, хороша.</li>
            </ul>
            Эти принципы помогают программистам писать качественный и понятный код на Python.
        </p>
        <img src="''' + url_for('static', filename='python.png') + '''">

        <footer>
            &copy; Полина Топорнина, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/raccoon")
def raccoon():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Факты о енотиках :З</h1>
        <p>
            Еноты могут издавать более пятидесяти разных звуков для общения! 
            Они шипят, мурлычут и рычат, но особенно «разговорчивы» еноты тогда, 
            когда конкурируют за пищу.
        </p>

        <p>
            У енотов очень высокий IQ для млекопитающих – выше, чем у кошек, и чуть ниже, 
            чем у обезьян. Они могут открывать контейнеры, поднимая крышки лапами. 
            Исследования даже показывают, что еноты способны помнить решения каких-либо 
            задач в течение трех лет.
        </p>

        <p>
            Еноты умеют развивать скорость до 25 км в час, причем даже, когда они карабкаются 
            по деревьям! Они могут упасть с высоты 40 м и остаться невредимыми. Еноты также 
            очень быстро плавают. Все эти умения они выработали для того, чтобы быстро удрать 
            после кражи пищи!
        </p>
        <img src="''' + url_for('static', filename='raccoon.jpg') + '''">

        <footer>
            &copy; Полина Топорнина, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''
