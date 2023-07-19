from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from stores.models import Store


def store_list(request):
    print("store_list", request.method, request)
    stores = Store.objects.all()
    return render(request, "store_list.html", {"stores": stores})



def add_store(request):
    if request.method == "POST":
        name = request.POST["name"]        

        store = Store(
            name = name,
        )
        store.save()

        return redirect("/")
    else:
        return render(request, "add_store.html")
    
def view_employees(request, store_id):
    try:
        store = get_object_or_404(Store, id=store_id)
        employees = store.employees.all()
        return render(request, "store_employees.html", {'store': store, 'employees': employees})
    except Http404:
        return render(request, "stores_404.html")
