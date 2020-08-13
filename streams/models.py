from django.db import models

# Create your models here.
class Stream(models.Model):
    stream_id=models.AutoField(primary_key=True,unique=True,verbose_name='Stream')
    stream_name=models.CharField(max_length=10, verbose_name='Stream', unique=True)

