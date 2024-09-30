from django.shortcuts import render,HttpResponse
from rest_framework import generics 
from .models import Students
from .serializers import studentclass
# Create your views here.

def index(request):
    return HttpResponse("Welcome to the Student API. Go to /api/students/ to see the student list.")

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = studentclass

class StudentDeleteView(generics.DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = studentclass
    lookup_field = 'id'



