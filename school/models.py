from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30, null=False)
    rg = models.CharField(max_length=9, null=False)
    cpf = models.CharField(max_length=12)
    born_date = models.DateField()

    def __str__(self):
        return self.name


class Curse(models.Model):
    LEVEL = (
        ("B", "Basic"),
        ("I", "Intermed"),
        ("A", "Advanced")
    )
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    curse_code = models.CharField(max_length=10, null=False)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default="B")

    def __str__(self):
        return self.description

class Registration(models.Model):
    PERIOD = (
        ("M", "Morning"),
        ("A", "Afternoon"),
        ("N", "Night")
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    curse = models.ForeignKey(Curse, on_delete=models.CASCADE)
    period = models.CharField(max_length=1, choices=PERIOD, blank=False, null=False, default="M")