from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your models here.
class Passwd_Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    site_name = models.CharField(max_length=50)
    site_url = models.URLField()
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=20)
    
    def save(self, *args, **kwargs):
        self.passwd = make_password(self.passwd)
        super(Passwd_Manager,self).save(*args,**kwargs)

    def __str__(self):
        return self.site_name
