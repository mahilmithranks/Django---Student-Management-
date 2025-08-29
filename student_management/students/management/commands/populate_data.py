from django.core.management.base import BaseCommand
from students.models import Department, Course, Student
import random

class Command(BaseCommand):
    help = 'Populate departments, courses, and students with sample data'

    def handle(self, *args, **kwargs):
        departments = [
            "CSE", "ECE", "EEE", "MECH", "CIVIL",
            "IT", "BIO", "CHEM", "AERO", "META",
            "ARCH", "Kalvium"
        ]

        courses = [
            {"name": "Python Programming", "department": "CSE"},
            {"name": "Data Structures", "department": "CSE"},
            {"name": "Electronics Basics", "department": "ECE"},
            {"name": "Thermodynamics", "department": "MECH"},
            {"name": "Structural Engineering", "department": "CIVIL"},
            {"name": "Biochemistry", "department": "BIO"},
            {"name": "Organic Chemistry", "department": "CHEM"},
        ]

        # Create Departments
        dept_objs = {}
        for dept_name in departments:
            dept, created = Department.objects.get_or_create(name=dept_name)
            dept_objs[dept_name] = dept
            if created:
                self.stdout.write(self.style.SUCCESS(f'Department created: {dept_name}'))

        # Create Courses
        course_objs = []
        for course in courses:
            try:
                dept = dept_objs[course["department"]]
                c, created = Course.objects.get_or_create(name=course["name"], department=dept)
                course_objs.append(c)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Course created: {course["name"]}'))
            except KeyError:
                self.stdout.write(self.style.ERROR(f'Department not found for course: {course["name"]}'))

        # Create Students
        names = ["Arun", "Divya", "Karthik", "Meena", "Pranav", "Swathi", "Vignesh", "Harini", "Mahesh", "Lakshmi"]
        for i in range(20):  # create 20 students
            course = random.choice(course_objs)
            dept = course.department
            Student.objects.get_or_create(
                name=random.choice(names) + f" {i+1}",
                age=random.randint(18, 24),
                email=f"student{i+1}@example.com",
                department=dept,
                course=course
            )

        self.stdout.write(self.style.SUCCESS('✅ Departments, courses, and students populated successfully!'))
