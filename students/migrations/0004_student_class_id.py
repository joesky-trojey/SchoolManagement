# Generated by Django 2.2.6 on 2020-06-17 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20200616_1151'),
        ('students', '0003_remove_student_class_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forms.Forms', verbose_name='Class'),
        ),
    ]