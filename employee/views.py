# employee/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .form import EmployeeForm
from django.db.models import Q


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})


def employee_list(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(department__icontains=query) |
            Q(email__icontains=query) 
        )
    else:
        employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees, 'query': query})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def edit_employee(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'edit_employee.html', {'form': form})

def delete_employee(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('employee_list')
    return render(request, 'confirm_delete.html', {'employee': emp})
