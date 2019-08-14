from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json

from typing import Dict, Any, Union

from django.shortcuts import render, HttpResponse
from dwebsocket.decorators import accept_websocket

import asyncio
import websockets
import mysql.connector
import json
import logging

logging.basicConfig()

logger = logging.getLogger("mylogger")

db = mysql.connector.connect(user='root', host='localhost', password='lovedog', database='campus')

resp_list = []

# stud_homepage
'''
    web -> node
{
'state': 'web'
'action':'get',
'infor': 'student',
'target': 'all',
'name':
}
    node -> web
{
'state': 'schoolserver',
'action': 'get',
'infor': 'student',
'name':
'id':
'year':
'major':
'course':
'teacher':
'grade':
}
'''


async def stud_homepage(name):
    cursor_basic = db.cursor(buffered = True)
    cursor_course = db.cursor(buffered = True)
    query_basic: str = ("SELECT student_id, grade, major FROM tab_stud_basic_info "
                        "WHERE name='{}'".format(name))

    query_course: str = ("SELECT course_code, teacher_name, grades FROM tab_stud_course_info "
                         "WHERE student_name='{}'".format(name))
    cursor_basic.execute(query_basic)
    cursor_course.execute(query_course)

    resp = dict(state='schoolserver', action='get', infor='student')

    for (student_id, grade, major) in cursor_basic:
        resp['name'] = name
        resp['id'] = student_id
        resp['year'] = grade
        resp['major'] = major
        
    for (course_code, teacher_name, grades) in cursor_course:
        resp['course'] = course_code
        resp['teacher'] = teacher_name
        resp['grade'] = grades

        
    resp_list.append(json.dumps(resp))
    logger.info(f"> {str(resp)}")


# tchr_homepage
'''
    web -> node

{
'state': 'web',
'action': 'get',
'infor': 'teacher',
'target': 'all',
'name':
}

    node -> web

{
'state': 'schoolserver',
'action': 'get',
'infor': 'teacher',
'name':
'title':
'course': [course1, course2, ...]
}
'''

async def tchr_homepage(name):
    cursor_basic = db.cursor(buffered = True)
    cursor_course = db.cursor(buffered = True)
    query_basic: str = ("SELECT title FROM tab_tchr_basic_info "
                        "WHERE name='{}'".format(name))
    query_course: str = ("SELECT course_code FROM tab_tchr_course_info "
                        "WHERE name='{}'".format(name))
    cursor_basic.execute(query_basic)
    cursor_course.execute(query_course)

    resp = {'state': 'schoolserver', 'action': 'get', 'infor': 'teacher', 'name':name}

    for title in cursor_basic:
        resp['title'] = title
    for course_code in cursor_course:
        resp['course'] = course_code

    resp_list.append(json.dumps(resp))
    logger.info(f"> {str(resp)}")

# tchr_change_grade
'''
    web -> node
{
'state': 'web',
'action': 'change',
'infor': 'student',
'target': 'grade',
'name':
'course':
'grade':
}
    node -> web
{
'state': 'web',
'action': 'change',
'infor': 'student',
'result': 'success'
}
'''

async def tchr_change_grade(name, course, grade):
    cursor = db.cursor(buffered = True)
    query: str = ("UPDATE tab_stud_course_info SET grades={} WHERE student_name='{}' AND course_code='{}'".format(grade, name, course))
    cursor.execute(query)

    resp = dict(state='web', action='change', infor='student', result='success')

    resp_list.append(json.dumps(resp))
    logger.info(f"> {str(resp)}")

# tchr_check_course
'''
    web -> node
{
'state': 'web',
'action': 'get',
'infor': 'studentlist',
'target': 'course',
'course':
}
    node -> web
{
'state': 'web',
'action': 'get',
'infor': 'studentlist',
'result': [name1, name2, ...]
}
'''

async def tchr_check_course(course):
    cursor = db.cursor(buffered = True)
    query: str = ("SELECT student_name FROM tab_stud_course_info WHERE course_code='{}'".format(course))
    cursor.execute(query)

    student_list = [student_name for student_name in cursor]

    resp = dict(state='web', action='get', infor='studentlist', result=student_list)

    resp_list.append(json.dumps(resp))
    logger.info(f"> {str(resp)}")

# sch_check_stud
'''
    web -> node
{
'state': 'web',
'action': 'get',
'infor': 'student',
'target': 'all',
'name':
}
    node -> web
{ 
'state':'schoolserver', 
'action':'get', 
'infor':'student', 
'name':
'id':
'year':
'major': 
'course': 
'teacher': 
'grade':
} 
'''

# TODO same as stud_homepage ?
async def sch_check_stud(name):
    cursor_basic = db.cursor(buffered = True)
    cursor_course = db.cursor(buffered = True)
    query_basic: str = ("SELECT student_id, grade, major FROM tab_stud_basic_info "
                        "WHERE name='{}'".format(name))

    query_course: str = ("SELECT course_code, teacher_name, grades FROM tab_stud_course_info "
                         "WHERE student_name='{}'".format(name))
    cursor_basic.execute(query_basic)
    cursor_course.execute(query_course)

    resp = dict(state='schoolserver', action='get', infor='student')

    for (student_id, grade, major) in cursor_basic:
        resp['name'] = name
        resp['id'] = student_id
        resp['year'] = grade
        resp['major'] = major
        
    for (course_code, teacher_name, grades) in cursor_course:
        resp['course'] = course_code
        resp['teacher'] = teacher_name
        resp['grade'] = grades

        
    resp_list.append(json.dumps(resp))
    logger.info(f"> {str(resp)}")

# sch_check_tchr
'''
    web -> node
{ 
“state”:”web”, 
“action”:”get”, 
“infor”:”teacher”, 
“target”:”all” 
“name”: 
} 
    node -> web
{ 
“state”:”schoolserver”, 
“action”:”get”, 
“infor”:"teacher”, 
“name”: 
“title”: 
“course”:[course1,course2....] 
} 

'''

# TODO same as tchr_homepage ?
async def sch_check_tchr(name):
    cursor_basic = db.cursor(buffered = True)
    cursor_course = db.cursor(buffered = True)
    query_basic: str = ("SELECT title FROM tab_tchr_basic_info "
                        "WHERE name='{}'".format(name))
    query_course: str = ("SELECT course_code FROM tab_tchr_course_info "
                        "WHERE name='{}'".format(name))
    cursor_basic.execute(query_basic)
    cursor_course.execute(query_course)

    resp = {'state': 'schoolserver', 'action': 'get', 'infor': 'teacher', 'name':name}

    for title in cursor_basic:
        resp['title'] = title
    for course_code in cursor_course:
        resp['course'] = course_code

    resp_list.append(json.dumps(resp))
    logger.info(f"> {str(resp)}")


# sch_change_stud
'''
    web -> node
{ 
“state”:”webserver”, 
“action”:”change”, 
“target”:”grade”,(course,id,year........) 
“infor”:”student” 
“name”: 
“course”: 
“grade”: 
} 
    node -> web
{ 
“state”:”webserver”, 
“action”:”change” 
“target”:”grade” (course,id,year........) 
“infor”:”student” 
“result”:”success” 
} 

'''

async def sch_change_stud(target, **kwargs):
    cursor = db.cursor(buffered = True)

    resp = dict(state='web', action='change', target=target, infor='student', result='success')

    # paras: name, grade, course
    if target == 'grade':
        query = (
            f"UPDATE tab_stud_course_info SET grades={kwargs['grade']} WHERE student_name={kwargs['name']} AND course_code={kwargs['course']}")
    # paras: orig_course, target_course, name
    elif target == 'course':
        query = "UPDATE tab_stud_course_info SET course_code='{}' WHERE student_name='{}' AND course_code='{}'".format(kwargs['target_course'],
                                                                                                      kwargs['name'],
                                                                                                      kwargs['orig_course'])
    # paras: orig_id, target_id, name
    elif target == 'id':
        query = "UPDATE tab_stud_basic_info SET student_id='{}' WHERE student_name='{}' AND student_id={}".format(kwargs['orig_id'],
                                                                                                   kwargs['name'],
                                                                                                   kwargs['target_id'])
    # paras: orig_year, targer_year, name
    elif target == 'year':
        query = "UPDATE tab_stud_basic_info SET grade={} WHERE student_name='{}' AND grade={}".format(kwargs['orig_year'],
                                                                                       kwargs['name'],
                                                                                       kwargs['target_year'])
    cursor.execute(query)

    resp_list.append(json.dumps(resp))
    logger.info(f"> {str(resp)}")



# sch_change_tchr
'''
    web ->node 
{ 
“state”:”webserver”, 
“action”:”change”, 
“target”:”title”,(course,paper........) 
“infor”:”teacher” 
“name”: 
“course”: 
} 
    Node -> web 
{ 
“state”:”webserver”, 
“action”:”change” 
“target”:”title”,(course,paper........) 
“infor”:”teacher” 
“result”:”success” 
} 
'''

async def sch_change_tchr(target, **kwargs):
    cursor = db.cursor(buffered = True)

    resp = dict(state='web', action='change', target=target, infor='teacher', result='success')

    # paras: orig_title, name, target_title
    if target == "title":
        query = "UPDATE tab_tchr_basic_info SET title='{}' WHERE name='{}', title='{}'".format(kwargs['target_title'],
                                                                                         kwargs['name'],
                                                                                         kwargs['orig_title'])
    # paras: orig_course, target_course, name
    elif target == 'course':
        query = ("UPDATE tab_tchr_basic_info SET course_code='{}' WHERE name='{}', course_code='{}'".
                 format(kwargs['target_title'],
                        kwargs['name'],
                        kwargs['orig_title']))
    cursor.execute(query)

    resp_list.append(json.dumps(resp))
    logger.info(f"> {json.dumps(resp)}")

# firm_check_certificate
'''
    web -> node 
  { 
“state”:”web”, 
“action”:”get”, 
“infor”:”certification”, 
“target”:”all” 
“certificationID”: 
} 
    Node -> web 
{ 
“state”:”employerserver”, 
“action”:”get”, 
“infor”: 'certification', 
“certificationID”: 
“result”:”successful”(“failed”) 
} 
'''

async def firm_check_certificate(certificationID):
    cursor = db.cursor(buffered = True)

    resp = dict(state='employerserver', action='get', infor='certification')

    query = "SELECT certificate_id FROM tab_certificate WHERE certificate_id='{}'".format(certificationID)

    cursor.execute(query)

    certificate_list = [certification for certification in cursor]
    if len(certificate_list) == 0:
        resp['result'] = 'failed'
    else:
        resp['result'] = 'success'
        
    resp_list.append(json.dumps(resp))
    logger.info(f"> {str(resp)}")
    
    
class DrawConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        recv = json.loads(text_data)
        logging.info("start receiving")
        if recv['action'] == 'get' and recv['infor'] == 'student' and recv['target'] == 'all':
            await stud_homepage(recv['name'])
        elif recv['action'] == 'get' and recv['infor'] == 'teacher' and recv['target'] == 'all':
            tchr_homepage(recv['name'])
        elif recv['action'] == 'change' and recv['infor'] == 'student' and recv['target'] == 'grade':
            await tchr_change_grade(recv['name'], recv['course'], recv['grade'])
        elif recv['action'] == 'get' and recv['infor'] == 'studentlist' and recv['target'] == 'course':
            await tchr_check_course(recv['course'])
        elif recv['action'] == 'change' and recv['infor'] == 'student' and recv['target'] != 'grade':
            if recv['target'] == 'course':
                await sch_change_stud(recv['target'], recv['target_course'], recv['name'], recv['orig_course'] )
            elif recv['target'] == 'id':
                await sch_change_stud(recv['target'], recv['target_id'], recv['name'], recv['orig_id'])
            elif recv['target'] == 'year':
                await sch_change_stud(recv['target'], recv['target_year'], recv['name'], recv['orig_year'])
        elif recv['action'] == 'change' and recv['infor'] == 'teacher':
            if recv['target'] == 'title':
                await sch_change_tchr(recv['target'], recv['orig_title'], recv['name'], recv['target_title'])
            elif recv['target'] == 'course':
                await sch_change_tchr(recv['target'], recv['orig_course'], recv['name'], recv['target_course'])
        elif recv['infor'] == 'certification':
            await firm_check_certificate(recv['certificationID'])
        resp = resp_list[0]
        resp_list.pop(0)
        await self.send(text_data=resp)

    async def disconnect(self, close_code):
        # Called when the socket closes
        await self.close()
        


