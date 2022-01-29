from django.db import models

# Create your models here.

class student(models.Model):
    s_name = models.CharField(max_length=50)


class Teacher(models.Model):
    t_name = models.CharField(max_length=50)


class College(models.Model):
    cl_name = models.CharField(max_length=50)

