from school.views import StudentsViewSet, CursesViewSet, RegistrationViewSet, RegistrationStudentsList, StudentsRegistrationList
from rest_framework import routers

from django.contrib import admin
from django.urls import path, include


router = routers.DefaultRouter()
router.register('student', StudentsViewSet, basename='students')
router.register('curse', CursesViewSet, basename='curses')
router.register('registration', RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('', include(router.urls)),
    path('student/<int:pk>/registrations/', RegistrationStudentsList.as_view()),
    path('curse/<int:pk>/registrations/', StudentsRegistrationList.as_view()),
    path('admin/', admin.site.urls),
]
