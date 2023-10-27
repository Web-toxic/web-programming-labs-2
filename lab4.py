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


@lab4.route('/lab4/grain_order')
def grain_order():
    return render_template('grain_order.html')


@lab4.route('/process_order', methods=['POST'])
def process_order():
    grain_type = request.form['grainType']
    weight = request.form['weight']

    if not weight:
        return "Ошибка: не введён вес. <a href='/lab4/grain_order'>Вернуться к заказу</a>"
    
    weight = float(weight)

    number = 0

    if weight <= 0:
        return "Ошибка: неверное значение веса. <a href='/lab4/grain_order'>Вернуться к заказу</a>"

    price_per_ton = 0
    if grain_type == 'ячмень':
        price_per_ton = 12000
    elif grain_type == 'овёс':
        price_per_ton = 8500
    elif grain_type == 'пшеница':
        price_per_ton = 8700
    elif grain_type == 'рожь':
        price_per_ton = 14000

    if weight > 500:
        return "Ошибка: такого объёма сейчас нет в наличии. <a href='/lab4/grain_order'>Вернуться к заказу</a>"
    elif weight > 50:
        total_price = weight * price_per_ton * 0.9
        message = f"Заказ успешно сформирован. Вы заказали зерно: {grain_type}. Вес: {weight} т. Сумма к оплате: {total_price} руб. (Применена скидка 10% за большой объём)"
    else:
        total_price = weight * price_per_ton
        message = f"Заказ успешно сформирован. Вы заказали зерно: {grain_type}. Вес: {weight} т. Сумма к оплате: {total_price} руб."

    return f"<h3>{message}</h3><br><a href='/lab4/grain_order'>Вернуться к заказу</a>"


