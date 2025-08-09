from django.db import models

# Create your models here.

class UserLogin(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_mnum = models.CharField(max_length=15)
    user_uname = models.CharField(max_length=30)
    user_psw = models.CharField(max_length=15)
    user_pic = models.ImageField(upload_to='images/')
    user_state = models.CharField(max_length=30)
    
    
    
class TechLogin(models.Model):
    tech_id = models.AutoField(primary_key=True)
    tech_name = models.CharField(max_length=40)
    tech_email = models.CharField(max_length=50)
    tech_mnum = models.CharField(max_length=15)
    tech_dept = models.CharField(max_length=40)
    tech_exp = models.CharField(max_length=20)
    tech_add = models.CharField(max_length=200)
    tech_pic = models.ImageField(upload_to='images/')
    tech_uravl = models.BooleanField(default=False)
    tech_uname = models.CharField(max_length=30)
    tech_psw = models.CharField(max_length=30)