# Generated by Django 2.0.4 on 2018-06-23 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0003_auto_20180623_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='car',
            name='patent',
            field=models.CharField(max_length=6),
        ),
    ]
