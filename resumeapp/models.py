from django.db import models
from django.db.models import CharField


class resumeprofile(models.Model):
    fullname=models.CharField(max_length=200)
    skills = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(max_length=255,blank=True, null=True)
    phone = models.CharField(max_length=10,blank=True, null=True)
    address=models.CharField(max_length=200,blank=True, null=True)
    universityCollege=models.CharField(max_length=200,blank=True, null=True)
    DegreeCertification=models.CharField(max_length=200,blank=True, null=True)
    graduation=models.CharField(max_length=200,blank=True, null=True)
    coursetitle=models.CharField(max_length=200,blank=True, null=True)
    projecttitle=models.CharField(max_length=200,blank=True, null=True)
    projectdescription=models.CharField(max_length=200,blank=True, null=True)
    prjectimg=models.ImageField(max_length=200,blank=True,null=True)
    prjectlink=models.URLField(max_length=200,blank=True,null=True)





def __str__(self):
    return '{}'.format(self.fullname)