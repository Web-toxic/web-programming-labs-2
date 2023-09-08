from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
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

            <ol>
                <li>
                    <a href="http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа 1</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab2" target="_blank">Лабораторная работа 2</a>
                </li>
            </ol>
        </main>

        <footer>
            &copy; Полина Топорнина, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
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

        <footer>
            &copy; Полина Топорнина, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""