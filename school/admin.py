from django.contrib import admin
from school.models import Student, Curse


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'born_date')
    list_display_links = ('id', 'name')

    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Student, Students)


class Curses(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'level', 'curse_code')
    list_display_links = ('curse_code', 'name')

    search_fields = ('name', 'curse_code',)


admin.site.register(Curse, Curses)
