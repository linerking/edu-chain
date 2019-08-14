# chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
  url('login_school/', views.login_school, name='login_school'),
  url('choose_way/', views.choose_way, name='choose_way'),
  url('employer_search/', views.employer_search, name='employer_search'),
  url('employer_search_result/', views.employer_search_result, name='employer_search_result'),
  url('excel_upload/', views.excel_upload, name='excel_upload'),
  url('login_employer/', views.login_employer, name='login_employer'),
  url('manual_upload/', views.manual_upload, name='manual_upload'),
  url('school_main/', views.school_main, name='school_main'),
  url('student_change/', views.student_change, name='student_change'),
  url('student_infor/', views.student_infor, name='student_infor'),
  url('student_main/', views.student_main, name='student_main'),
  url('student_search/', views.student_search, name='student_search'),
  url('teacher_main/', views.teacher_main, name='teacher_main'),
  url('teacher_search/', views.teacher_search, name='teacher_search'),
  url('teacher_upload/', views.teacher_upload, name='teacher_upload'),
  url('permission/', views.add_permission, name='add_permission'),
  url('school_login',views.school_login,name="school_login"),
  url('employer_login',views.employer_login,name="employer_login"),
  url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

