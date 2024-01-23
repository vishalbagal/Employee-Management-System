
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department, Salary

def base(request):
    return render(request,'base.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'department_detail.html', {'department': department})

def salary_list(request):
    salaries = Salary.objects.all()
    return render(request, 'salary_list.html', {'salaries': salaries})

def salary_detail(request, salary_id):
    salary = get_object_or_404(Salary, pk=salary_id)
    return render(request, 'salary_detail.html', {'salary': salary})
