from django.db import models

# Create your models here.

class Exam(models.Model):
    pk_exam = models.AutoField(primary_key=True)
    alumno = models.CharField(max_length=50, blank=False, null=False)
    grado = models.CharField(max_length=50, blank=False, null=False)
    curso = models.CharField(max_length=100, blank=False, null=True)
    observaciones = models.TextField(blank=False, null=True)