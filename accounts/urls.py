from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('student/', views.student_create),
    path('graduate/', views.graduate_create),

    path('export/students/', views.export_students_excel),
    path('export/graduates/', views.export_graduates_excel),
    
    path('students/', views.student_list),
    path('graduates/', views.graduate_list),
    
    path('student/delete/<int:id>/', views.student_delete),
    path('graduate/delete/<int:id>/', views.graduate_delete),
    
    path('student/edit/<int:id>/', views.student_edit),
    path('graduate/edit/<int:id>/', views.graduate_edit),
]