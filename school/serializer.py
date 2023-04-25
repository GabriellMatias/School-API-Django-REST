from rest_framework import serializers
from school.models import Student, Curse


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'cpf', 'born_date', 'rg']


class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = '__all__'
