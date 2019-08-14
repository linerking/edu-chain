import asyncio
import mysql.connector
import json

db = mysql.connector.connect(user='root', host='localhost', password='lovedog', database='campus')

resp_list = []

def stud_homepage(name):
    cursor_basic = db.cursor(buffered = True)
    cursor_course = db.cursor(buffered = True)

    query_basic = ("SELECT student_id, grade, major FROM tab_stud_basic_info "
                        "WHERE name='{}'".format(name))

    query_course = ("SELECT course_code, teacher_name, grades FROM tab_stud_course_info "
                         "WHERE student_name='{}'".format(name))
    cursor_basic.execute(query_basic)
    cursor_course.execute(query_course)

    resp = dict(state='schoolserver', action='get', infor='student')

    for (student_id, grade, major) in cursor_basic:
        resp['name'] = name
        resp['id'] = student_id
        resp['year'] = grade
    for (course_code, teacher_name, grades) in cursor_course:
        resp['course'] = course_code
        resp['teacher'] = teacher_name
        resp['grade'] = grades
        
    resp_list.append(json.dumps(resp))

stud_homepage("student1")

print(resp_list[0])
