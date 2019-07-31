from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def logging_School(request):
    return render(request, 'draw/logging_school.html', {})
  
  
def logging_Education(request):
    return render(request, 'draw/logging_Education.html', {})
  
  
def choose_way(request):
    return render(request, 'draw/choose_way.html', {})
  
  
def Education_change(request):
    return render(request, 'draw/Education_change.html', {})
  
  
def employer_main(request):
    return render(request, 'draw/employer_main.html', {})
  
  
def employer_search_result(request):
    return render(request, 'draw/employer_search_result.html', {})
  
  
def employer_search(request):
    return render(request, 'draw/employer_search.html', {})
  
  
def excel_upload(request):
    return render(request, 'draw/excel_upload.html', {})
  
  
def logging_employer(request):
    return render(request, 'draw/logging_employer.html', {})
  
  
def manual_upload(request):
    return render(request, 'draw/manual_upload.html', {})
  
  
def school_main(request):
    return render(request, 'draw/school_main.html', {})
  
  
def student_change(request):
    return render(request, 'draw/student_change.html', {})
  
  
def student_infor(request):
    return render(request, 'draw/student_infor.html', {})
  
  
def student_main(request):
    return render(request, 'draw/student_main.html', {})
  
  
def student_search(request):
    return render(request, 'draw/student_search.html', {})
  
  
def Education_main(request):
    return render(request, 'draw/Education_main.html', {})
  
  
def teacher_main(request):
    return render(request, 'draw/teacher_main.html', {})
  
  
def teacher_search(request):
    return render(request, 'draw/teacher_search.html', {})
  
  
def teacher_upload(request):
    return render(request, 'draw/teacher_upload.html', {})

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })