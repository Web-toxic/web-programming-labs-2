from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    
    errors = {}
    card = request.args.get('card')
    name = request.args.get('name')
    cvv = request.args.get('cvv')
    if card == '':
        errors['card'] = 'Введите данные'
    if name == '':
        errors['name'] = 'Введите данные'
    if cvv == '':
        errors['cvv'] = 'Введите данные'
    return render_template('pay.html', price=price, card=card, name=name, cvv=cvv, errors=errors)


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    name = request.args.get('name')
    age = request.args.get('age')
    from_where = request.args.get('from_where')
    where = request.args.get('where')
    date = request.args.get('date')
    if name == '':
        errors['name'] = 'Введите данные'
    if age == '':
        errors['age'] = 'Введите данные'
    if from_where == '':
        errors['from_where'] = 'Введите данные'
    if where == '':
        errors['where'] = 'Введите данные'
    if date == '':
        errors['date'] = 'Введите данные'

    return render_template('ticket.html', name=name, age=age, from_where=from_where, where=where, date=date, errors=errors)

@lab3.route('/lab3/ready_ticket')
def ready_ticket():
    return render_template('ready_ticket.html')
