from rest_framework import serializers
from school.models import Student, Curse, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'cpf', 'born_date', 'rg']


class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class RegistrationStudentsListSerializer(serializers.ModelSerializer):
    curse = serializers.ReadOnlyField(source='curse.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['curse', 'period']

    def get_period(self, obj):
        return obj.get_period_display()


class StudentsRegistrationInCurseListSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = ['student_name']
