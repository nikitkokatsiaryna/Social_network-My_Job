# Generated by Django 3.0.6 on 2020-09-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200909_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='e_mail',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
    ]
