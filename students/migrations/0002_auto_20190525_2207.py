# Generated by Django 2.2 on 2019-05-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Absent', 'A'), ('Present', 'P')], max_length=10),
        ),
    ]