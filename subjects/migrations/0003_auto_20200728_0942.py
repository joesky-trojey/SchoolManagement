# Generated by Django 3.0.8 on 2020-07-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20200728_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='shorthand',
            field=models.CharField(default='', max_length=10, verbose_name="Subject's shorhand"),
        ),
    ]
