from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('quiz/', views.quiz_question, name='quiz_question'),
    path('done/', views.done, name='done'),
    path('staff/', views.staff_gate, name='staff_gate'),
    path('staff/list/', views.staff_list, name='staff_list'),
    path('staff/exit/', views.staff_exit, name='staff_exit'),
]
