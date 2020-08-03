from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils.text import slugify


class Experience(models.Model):
    position = models.CharField(max_length=50)
    type_employment = models.CharField(max_length=2)
    company = models.CharField(max_length=100)
    region = models.CharField(max_length=50, blank=True)
    date_start = models.DateField(default=datetime.now)
    date_end = models.DateField(default=datetime.now)
    description = models.TextField(blank=True)

    user = models.ForeignKey(User, related_name='experiences_created', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.position)
            super(Experience, self).save(*args, **kwargs)


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    date_start = models.DateField(default=datetime.now, blank=True)
    date_end = models.DateField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)


# class Account(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     experience = models.ForeignKey(Experience, on_delete=models.CASCADE, default="")
