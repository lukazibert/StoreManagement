from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.store_list, name='store_list'),
    path('add_store/', views.add_store, name='add_store'),
    path('view_employees/<int:store_id>/', views.view_employees, name='view_employees'),
    path('store_employees/<int:store_id>/', views.view_employees, name='store_employees')
]