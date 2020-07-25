from django.db import models
from forms.models import Forms
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):

    admission_number=models.PositiveIntegerField(primary_key=True, unique=True, verbose_name='Admission number')
    fname=models.CharField(max_length=30, verbose_name='First name')
    sname=models.CharField(max_length=30, verbose_name='Middle Name')
    surname=models.CharField(max_length=30)
    class_id=models.ForeignKey(Forms,verbose_name='Class', default=1,on_delete=models.CASCADE,)
    kcpe=models.PositiveIntegerField(verbose_name='Kcpe Marks',validators=[MinValueValidator(1),MaxValueValidator(500)])
    passport=models.FileField(max_length=200,upload_to='passports/',verbose_name='Passport Photo')
    stream_id=models.IntegerField(verbose_name='Stream')

    
    
    



# Create your models here.
