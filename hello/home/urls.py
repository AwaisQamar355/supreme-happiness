from django.contrib import admin
from django.urls import path
from .views import StudentListCreateView , StudentDeleteView
urlpatterns = [
    path('students/', StudentListCreateView.as_view() , name ='StudentListCreateView'),
    path('students/<int:id>', StudentDeleteView.as_view() , name ='StudentDeleteView'),
    
]


