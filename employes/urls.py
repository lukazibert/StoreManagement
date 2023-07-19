from django.urls import path
from . import views

app_name = 'employes'

urlpatterns = [
    path('add_employee/<int:store_id>', views.add_employee, name='add_employee'),
    path('edit_employee/<int:employee_id>/<int:store_id>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<int:employee_id>/<int:store_id>', views.delete_employee, name='delete_employee')
]