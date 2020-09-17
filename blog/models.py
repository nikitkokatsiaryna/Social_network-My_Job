from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django_fields import DefaultStaticImageField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    location = models.CharField(max_length=30)
    e_mail = models.EmailField(null=True, blank=True, default='')
    phone = models.CharField(max_length=20, blank=True)
    web_sites = models.URLField(max_length=200, blank=True)
    common_information = models.TextField(max_length=500, blank=True)
    profile_image = DefaultStaticImageField(blank=True, null=True, default_image_path='img/unnamed.jpg')


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Experience(models.Model):
    position = models.CharField(max_length=50)
    type_employment = models.CharField(max_length=2, null=True)
    company = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=50, blank=True)
    checkbox = models.BooleanField(blank=True, default=False)
    date_start = models.DateField(default=datetime.now, null=True)
    date_end = models.DateField(default=datetime.now, null=True)
    description = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, related_name='experiences_created', on_delete=models.CASCADE)


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    date_start = models.DateField(default=datetime.now, blank=True)
    date_end = models.DateField(default=datetime.now, blank=True)
    description = models.TextField(blank=True)

    user = models.ForeignKey(User, related_name='education_created', on_delete=models.CASCADE)


class Certificate(models.Model):
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    checkbox = models.BooleanField(blank=True, default=False)
    date_start = models.DateField(default=datetime.now, blank=True)
    date_end = models.DateField(default=datetime.now, blank=True)
    url_address = models.CharField(max_length=150, blank=True)

    user = models.ForeignKey(User, related_name='certificate_created', on_delete=models.CASCADE)


class Skill(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, related_name='skill_created', on_delete=models.CASCADE)
