from django.db import models

# Create your models here.

class Users(models.Model):
    firstname=models.CharField(max_length=20,name='first_name')
    lastname=models.CharField(max_length=20,name='last_name')
    age=models.IntegerField(name='age')
    gender=models.CharField(max_length=20,name='gender',default='NULL')
    dob=models.DateField(name='DOB')
    umail=models.EmailField(name='mailid',primary_key=True)
    pwd=models.CharField(max_length=20,name='password')

class Mails(models.Model):
    from_user=models.CharField(max_length=20)
    to_user=models.ForeignKey(Users,on_delete=models.CASCADE)
    content=models.CharField(max_length=1000)
    sent_at = models.DateTimeField(auto_now_add=True)