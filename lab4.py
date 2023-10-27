from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    

    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success.html')
    errors = 'Неверные логин или пароль'
    if username == '':
        errors = 'Введите логин'
    if password == '':
        errors = 'Введите пароль'
    
    
    return render_template('login.html', errors=errors, username=username, password=password)
 

@lab4.route('/lab4/refrigerator', methods=['GET', 'POST'])
def refrigerator(): 
    err = ''
    if request.method =='GET':
        return render_template('refrigerator.html', err=err)
    
    temperature = request.form.get('temperature')

    if temperature == '':
        err ='Не задана температура'
    else:
        temperature = int(temperature)
        if temperature < (-12):
            err ='Не удалось установить температуру — слишком низкое значение'
        elif temperature > (-1):
            err = 'Не удалось установить температуру — слишком высокое значение'
        elif (temperature >= (-12)) and (temperature <= (-9)):
            err = f'Установлена температура: {temperature}°С ❄️❄️❄️'
        elif (temperature >= (-8)) and (temperature <= (-5)):
            err = f'Установлена температура: {temperature}°С ❄️❄️'
        elif (temperature >= (-4)) and (temperature <= (-1)):
            err = f'Установлена температура: {temperature}°С ❄️'
    return render_template('refrigerator.html', temperature=temperature, err=err)