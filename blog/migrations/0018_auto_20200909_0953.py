# Generated by Django 3.0.6 on 2020-09-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200909_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='img/unnamed.jpg', null=True, upload_to=''),
        ),
    ]
