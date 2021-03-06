# Generated by Django 2.2.6 on 2020-06-15 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('admission_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fname', models.CharField(max_length=30)),
                ('sname', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('kcpe', models.IntegerField()),
                ('passport', models.CharField(max_length=200)),
                ('stream_id', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Form')),
            ],
        ),
    ]
