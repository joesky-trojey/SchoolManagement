# Generated by Django 3.0.8 on 2020-07-27 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0001_initial'),
        ('students', '0008_auto_20200724_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stream_id',
            field=models.ForeignKey(default='A', on_delete=django.db.models.deletion.CASCADE, to='streams.Stream', verbose_name='Stream'),
        ),
    ]