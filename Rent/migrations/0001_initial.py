# Generated by Django 2.0.4 on 2018-06-23 01:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=120)),
                ('color', models.CharField(max_length=120)),
                ('picture', models.ImageField(upload_to='car')),
                ('patent', models.CharField(max_length=6)),
                ('restriction', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('birthday', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('rut', models.CharField(max_length=8)),
                ('dv', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Executive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('birthday', models.DateField()),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(upload_to='picture_executive')),
                ('rut', models.CharField(max_length=8)),
                ('dv', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rent.Car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rent.Client')),
                ('executive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rent.Executive')),
            ],
        ),
    ]