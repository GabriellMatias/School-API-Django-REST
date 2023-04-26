from rest_framework import viewsets, generics
from school.serializer import StudentSerializer, CurseSerializer, RegistrationSerializer, \
    RegistrationStudentsListSerializer, StudentsRegistrationInCurseListSerializer
from school.models import Student, Curse, Registration
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """Printing all students"""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursesViewSet(viewsets.ModelViewSet):
    """Printing all Curses"""

    queryset = Curse.objects.all()
    serializer_class = CurseSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """Printing all Registrations"""

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationStudentsList(generics.ListAPIView):
    """Listing Registrations"""

    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = RegistrationStudentsListSerializer


class StudentsRegistrationList(generics.ListAPIView):
    """Listing Students in a curse"""

    def get_queryset(self):
        queryset = Registration.objects.filter(curse_id=self.kwargs['pk'])
        return queryset

    serializer_class = StudentsRegistrationInCurseListSerializer
