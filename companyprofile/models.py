from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User

# Create your models here.
class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    site = models.CharField(max_length=255,null=True)

class CompanyUsers(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    role = models.CharField(max_length=255)
    hr_rate = models.FloatField()