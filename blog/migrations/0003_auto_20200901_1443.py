# Generated by Django 3.0.6 on 2020-09-01 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_certificates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certificates',
            new_name='Certificate',
        ),
    ]
