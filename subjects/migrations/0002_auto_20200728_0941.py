# Generated by Django 3.0.8 on 2020-07-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='shorthand',
            field=models.CharField(default=models.CharField(max_length=20, unique=True, verbose_name='Subject'), max_length=10, verbose_name="Subject's shorhand"),
        ),
        migrations.AlterField(
            model_name='subject',
            name='optionality',
            field=models.CharField(max_length=1, verbose_name='Optionality'),
        ),
    ]
