from flask import Blueprint, jsonify, render_template, request, abort

lab8 = Blueprint('lab8',__name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')


courses = [
    {"name": "c++", "videos": 3,"price": 3000},
    {"name": "basic", "videos": 30,"price": 0},
    {"name": "c#", "videos": 8} #если цена не указана, то курс бесплатный
]


#Весь список курсов
@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses2():
    return jsonify (courses)


#Конкретный курс по номеру
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_courses3(course_num):
    if 0<= course_num < len(courses)-1:
        return courses[course_num]
    else:
        abort(404, "Course not found")


