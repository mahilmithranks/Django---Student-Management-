from rest_framework import viewsets
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer

# API ViewSet for CRUD operations
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Homepage view
def home(request):
    return render(request, "students/home.html")
