# Generated by Django 3.0.8 on 2020-07-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0002_auto_20200727_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='stream_name',
            field=models.CharField(max_length=10, unique=True, verbose_name='Stream'),
        ),
    ]
