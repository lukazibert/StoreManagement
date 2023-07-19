from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from employes.models import Employee
from stores.models import Store


def add_employee(request, store_id):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        date_of_birth = request.POST["date_of_birth"]
        gender = request.POST["gender"]
        store = Store.objects.get(id=store_id)

        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            store = store,
        )
        employee.save()
        store.employees.add(employee)

        return redirect("stores:view_employees", store_id=store_id)
    else:
        return render(request, "add_employee.html")


def edit_employee(request, employee_id, store_id):
    try:
        employee = get_object_or_404(Employee, id=employee_id)
        if request.method == "POST":
            employee.first_name = request.POST["first_name"]
            employee.last_name = request.POST["last_name"]
            employee.date_of_birth = request.POST["date_of_birth"]
            employee.gender = request.POST["gender"]

            employee.save()

            return redirect("stores:view_employees", store_id=store_id)
        else:
            return render(request, "edit_employee.html", {"employee": employee})
    except Http404:
        return render(request, "employees_404.html")


    
def delete_employee(request, employee_id, store_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect("stores:view_employees", store_id=store_id)
