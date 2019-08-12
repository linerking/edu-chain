from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login
from django.contrib.auth import *
from django.contrib.contenttypes.models import ContentType
from django.http import  HttpResponse
from django.contrib.auth.decorators import permission_required, login_required

import json

def login_school(request):
    return render(request, 'draw/login_school.html', {})
  
  
  
@login_required
@permission_required('auth.teacher')  
def choose_way(request):
    course = request.POST.get("course")
    return render(request, 'draw/choose_way.html', {"course":json.dumps(course)})
  
  
@login_required 
@permission_required('auth.employer')   
def employer_search_result(request):
    result = request.POST.get("result")
    return render(request, 'draw/employer_search_result.html', {"result":json.dumps(result)})
  
@login_required 
@permission_required('auth.employer')   
def employer_search(request):
    ID = request.POST.get("username")
    return render(request, 'draw/employer_search.html', {"ID":ID})
  
@login_required
@permission_required('auth.teacher')  
def excel_upload(request):
    return render(request, 'draw/excel_upload.html', {})
  
  
def login_employer(request):
    return render(request, 'draw/login_employer.html', {})
  
@login_required
@permission_required('auth.teacher')  
def manual_upload(request):
    course = request.POST.get("result")
    return render(request, 'draw/manual_upload.html', {"course":json.dumps(course)})
  
@login_required
@permission_required('auth.school') 
def school_main(request):
    return render(request, 'draw/school_main.html', {})
  
@login_required
@permission_required('auth.school')   
def student_change(request):
    name = request.POST.get("username")
    return render(request, 'draw/student_change.html', {"name":json.dumps(name)})
  
@login_required 
@permission_required('auth.student')   
def student_infor(request):
    infor = request.user.username
    return render(request, 'draw/student_infor.html', {"infor":json.dumps(infor)})
@login_required 
@permission_required('auth.student')  
def student_main(request):
    return render(request, 'draw/student_main.html', {})
  
@login_required
@permission_required('auth.school')   
def student_search(request):
    name = request.POST.get("username")
    return render(request, 'draw/student_search.html', {"name":json.dumps(name)})
  
  
@login_required
@permission_required('auth.teacher')
def teacher_main(request):
    return render(request, 'draw/teacher_main.html', {})
  
@login_required
@permission_required('auth.school')   
def teacher_search(request):
    return render(request, 'draw/teacher_search.html', {})
    
@login_required
@permission_required('auth.teacher')  
def teacher_upload(request):
    return render(request, 'draw/teacher_upload.html', {})

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
  
def employer_login(request):
    username = request.POST['username']
    password = request.POST['password']
 
    # Django提供的authenticate函数，验证用户名和密码是否在数据库中匹配
    user = authenticate(username=username, password=password)
 
    if user is not None:
        # Django提供的login函数，将当前登录用户信息保存到会话key中
        login(request, user)
        if user.has_perm('auth.employer'):
          return redirect('https://edu-chain-906870065650856.codeanyapp.com/draw/employer_search/')
        # 进行登录成功的操作，重定向到某处等
    else:
        # 返回用户名和密码错误信息
        return redirect('https://edu-chain-906870065650856.codeanyapp.com/draw/login_employer/')
def school_login(request):
    username = request.POST['username']
    password = request.POST['password']
 
    # Django提供的authenticate函数，验证用户名和密码是否在数据库中匹配
    user = authenticate(username=username, password=password)
 
    if user is not None:
        # Django提供的login函数，将当前登录用户信息保存到会话key中
        login(request, user)
        if user.has_perm('auth.student'):
          return redirect('https://edu-chain-906870065650856.codeanyapp.com/draw/student_main/')
        elif user.has_perm('auth.teacher'):
          return redirect('https://edu-chain-906870065650856.codeanyapp.com/draw/teacher_main/')
        elif user.has_perm('auth.school'):
          return redirect('https://edu-chain-906870065650856.codeanyapp.com/draw/school_main/')
        # 进行登录成功的操作，重定向到某处等
    else:
        # 返回用户名和密码错误信息
        return redirect('https://edu-chain-906870065650856.codeanyapp.com/draw/login_school/')
def add_permission(request):
    content_type = ContentType.objects.get_for_model(models.Group)
    permission1 = models.Permission.objects.create(
    codename='school',
    name='学校权限',
    content_type=content_type,
)
    student = models.Group.objects.filter(name='school').first()
    student.permissions.add(permission1)
    return HttpResponse('权限创建成功')
