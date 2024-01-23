
from django.contrib import admin
from .models import Department, Employee, Salary

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation', 'reporting_manager', 'department')
    search_fields = ('name', 'email')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'manager')
    search_fields = ('name',)

class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'start_date', 'end_date')
    search_fields = ('employee__name',)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salary, SalaryAdmin)
