from django.db import models

# Create your models here.
class user(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=True,blank=True,max_length=100)
    password=models.CharField(null=True,blank=True,max_length=100)
    email=models.CharField(null=True,blank=True , max_length=100)
    phno=models.CharField(null=True,blank=True,max_length=10)
    country=models.CharField(null=True,blank=True,max_length=100)


    def __str__(self):
        return self.name
    

class prd(models.Model):
    id=models.AutoField(primary_key=True)
    prd_name = models.CharField(null=True, blank=True, max_length=100)
    pri = models.CharField(null=True, blank=True, max_length=100)
    description=models.TextField(null=True, blank=True)
    prd_pic = models.ImageField(upload_to='media/', blank=True, null=True)
    
    def _str_(self):
        return self.prd_name