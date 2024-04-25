from django.db import models

# Create your models here.

class home(models.Model):
    s_no=models.IntegerField(max_length=70)
    first_name=models.CharField(max_length=70)
    last_name=models.CharField(max_length=70)
    email=models.EmailField(max_length=80)
