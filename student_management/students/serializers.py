from rest_framework import serializers
from .models import Student, Course, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)  # optional if you want department in course

    class Meta:
        model = Course
        fields = ['id', 'name', 'department']

class StudentSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'department', 'course', 'department_name', 'course_name']
