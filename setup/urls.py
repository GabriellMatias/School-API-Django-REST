from school.views import StudentsViewSet, CursesViewSet
from rest_framework import routers

from django.contrib import admin
from django.urls import path, include

#Create Default route
router = routers.DefaultRouter()
router.register('student', StudentsViewSet, basename='students')
router.register('curse', CursesViewSet, basename='curses')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
