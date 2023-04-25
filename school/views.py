from rest_framework import viewsets
from school.models import Student, Curse
from school.serializer import StudentSerializer, CurseSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """Printing all students"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CursesViewSet(viewsets.ModelViewSet):
    """Printing all Curses"""

    queryset = Curse.objects.all()
    serializer_class = CurseSerializer
