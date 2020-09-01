# Generated by Django 3.0.6 on 2020-09-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('department', models.CharField(max_length=150)),
                ('date_start', models.DateField(blank=True)),
                ('date_end', models.DateField(blank=True)),
                ('url_address', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
