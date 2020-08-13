from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_id=models.AutoField(primary_key=True,unique=True, verbose_name='Stream')
    subject_name=models.CharField(max_length=20, verbose_name='Subject Name', unique=True)
    shorthand=models.CharField(max_length=10, verbose_name='Subject\'s shorthand',default='')
    optionality=models.CharField(choices=(('','Select Optionality'),('1','Comparsory'),('0','Optional')),default='1',max_length=2)
