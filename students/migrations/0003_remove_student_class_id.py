# Generated by Django 2.2.6 on 2020-06-16 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200615_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='class_id',
        ),
    ]