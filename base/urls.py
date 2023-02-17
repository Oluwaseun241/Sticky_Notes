from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create_note'),
    path('delete/<int:pk>/', views.delete, name='delete_note'),
    path('update/<int:pk>/', views.update, name='update_note')
]
