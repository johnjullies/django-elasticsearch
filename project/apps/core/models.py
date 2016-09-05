from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class University(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior')
    )
    # note: incorrect choice in MyModel.create leads to creation of
    # incorrect record
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    age = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # various relationship models
    university = models.ForeignKey(University, null=True, blank=True)
    courses = models.ManyToManyField(Course, blank=True)
