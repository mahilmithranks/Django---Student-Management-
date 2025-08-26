from rest_framework import viewsets
from django.shortcuts import render
from .models import Student, Course, Department
from .serializers import StudentSerializer, CourseSerializer, DepartmentSerializer

# API ViewSets
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Homepage view
def home(request):
    return render(request, "students/home.html")
