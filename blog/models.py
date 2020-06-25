from django.db import models
from django.contrib.auth.models import User
from enum import Enum
from django.db import models


class TypeEmploymentChoice(Enum):
    Empty = '-'
    FD = 'Full work day'
    PE = 'Partial employment'
    BM = 'Businessman'
    F = 'Freelance'
    C = 'Contract'
    I = 'Internship'


class Experience(models.Model):
    position = models.CharField(max_length=50)
    type_employment = models.CharField(max_length=2, choices=[(tag, tag.value) for tag in TypeEmploymentChoice])
    company = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField()


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, default="")

