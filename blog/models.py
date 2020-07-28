from django.db import models
from django.contrib.auth.models import User
from enum import Enum
from django.db import models
from datetime import datetime


class Experience(models.Model):
    position = models.CharField(max_length=50)
    type_employment = models.CharField(max_length=2)
    company = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    date_start = models.DateField(default=datetime.now, blank=True)
    date_end = models.DateField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    date_start = models.DateField(default=datetime.now, blank=True)
    date_end = models.DateField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, default="")
