from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view , name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('std', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
