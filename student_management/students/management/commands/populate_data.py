from django.core.management.base import BaseCommand
from students.models import Department, Course

class Command(BaseCommand):
    help = 'Populate departments and courses with sample data'

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
        for dept_name in departments:
            dept, created = Department.objects.get_or_create(name=dept_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Department created: {dept_name}'))

        # Create Courses
        for course in courses:
            try:
                dept = Department.objects.get(name=course["department"])
                c, created = Course.objects.get_or_create(name=course["name"], department=dept)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Course created: {course["name"]}'))
            except Department.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Department not found for course: {course["name"]}'))

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully!'))
