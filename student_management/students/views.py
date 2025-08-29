from rest_framework import viewsets
from django.shortcuts import render
from django.db.models import Q
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

# Student List with Search + Filter
def student_list(request):
    students = Student.objects.all()
    departments = Department.objects.all()

    # Search by name/email
    query = request.GET.get("q", "")
    if query:
        students = students.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )

    # Filter by department
    dept_filter = request.GET.get("department", "all")
    if dept_filter != "all":
        students = students.filter(department__id=dept_filter)

    return render(request, "students/student_list.html", {
        "students": students,
        "departments": departments,
        "query": query,
        "dept_filter": dept_filter
    })
