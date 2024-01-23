from django.urls import path
from . import views

urlpatterns = [
    path('',views.base),
    path('employee/', views.employee_list, name='employee_list'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('department/', views.department_list, name='department_list'),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),
    path('salary/', views.salary_list, name='salary_list'),
    path('salary/<int:salary_id>/', views.salary_detail, name='salary_detail'),
]
