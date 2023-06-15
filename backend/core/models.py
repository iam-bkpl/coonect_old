from django.db import models
from django.contrib.auth.models import User

class AdminBank(models.Model):
  account_name = models.CharField(max_length=255)
  bank_name = models.CharField(max_length=255)
  branch = models.CharField(max_length=255)
  account_number = models.CharField(max_length=255)
  qr_code = models.ImageField(upload_to='admin_bank')
  
  
class Timing(models.Model):
  first_day = models.CharField(max_length=255)
  last_day = models.CharField(max_length=255)
  start_time = models.TimeField(auto_now=True)
  end_time = models.TimeField(auto_now=True)

class HomePageImage(models.Model):
  name = models.CharField(max_length=255, blank=True, null=True)
  image = models.ImageField(upload_to='home')

class AboutUs(models.Model):
  image = models.ImageField(upload_to='abouts/images', blank=True, null=True)
  text = models.TextField(blank=True, null=True)
  


# class SocialLink(models.Model):
#   name = models.CharField(max_length=255, blank=True, null=True)
#   link = models.URLField(blank=True,null=True)  

class Team(models.Model):
  image = models.ImageField(upload_to='team/images', blank=True, null=True)
  name = models.CharField(max_length=255)
  position = models.CharField(max_length=255, blank=True, null=True)
  facebook_link = models.URLField(blank=True, null=True, default="https://www.facebook.com/")
  instagram_link = models.URLField(blank=True, null=True, default="https://www.instagram.com/")
  linkedin_link = models.URLField(blank=True, null=True, default="https://www.linkedin.com/")


class Service(models.Model):
  name = models.CharField(max_length=255, blank=True, null=True)
  image = models.ImageField(upload_to='service/images')
  text = models.TextField()


class Partners(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='partner/images')
  

class Event(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True, default='Event Title')
  description = models.TextField(null=True, blank=True)
  image = models.ImageField(upload_to='event/images', blank=True,null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  hover_text = models.CharField(max_length=255, blank=True, null=True)
  date = models.DateTimeField()
  
class MainService(models.Model):
  name = models.CharField(max_length=255,blank=True, null=True)
  description = models.TextField(null=True, blank=True)
  image = models.ImageField(upload_to='mainService/images',null=True, blank=True)
  hover_text = models.CharField(max_length=255, blank=True, null=True)  
  location = models.CharField(max_length=255,null=True,blank=True)
  price = models.PositiveIntegerField(default=0)
  date = models.DateTimeField(auto_now=True)
  
    
class Contact(models.Model):
  phone = models.CharField(max_length=20)
  email = models.EmailField()
  address = models.CharField(max_length=255)



class Membership(models.Model):
  MEMBERSHIP_TYPE_INDIVIDUAL = 'individual'
  MEMBERSHIP_TYPE_FAMILY = 'family'
  MEMBERSHIP_TYPE_STUDENT = 'student'

  MEMBERSHIP_TYPE_CHOICES = [
    (MEMBERSHIP_TYPE_INDIVIDUAL, 'individual'),
    (MEMBERSHIP_TYPE_FAMILY, 'family'),
    (MEMBERSHIP_TYPE_STUDENT, 'student'),
    ]
  
  MEMBERSHIP_DURATION_ANNUAL= 'annual'
  MEMBERSHIP_DURATION_SEMI_ANNUAL = 'semi-annual'
  MEMBERSHIP_DURATION_MONTHLY = 'monthly'

  MEMBERSHIP_DURATION_CHOICES = [
    (MEMBERSHIP_DURATION_ANNUAL, 'annual'),
    (MEMBERSHIP_DURATION_SEMI_ANNUAL, 'semi-annual'),
    (MEMBERSHIP_DURATION_MONTHLY, 'monthly'),
    ]
  
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  address = models.CharField(max_length=255, blank=True, null=True)
  phone = models.CharField(max_length=255, blank=True, null=True)
  profile = models.ImageField(upload_to='PP')
  passport_front = models.FileField(upload_to='passport')
  passport_back = models.FileField(upload_to='passport')
  membership_type = models.CharField(max_length=255, choices=MEMBERSHIP_TYPE_CHOICES, default=MEMBERSHIP_TYPE_INDIVIDUAL)
  membership_duration = models.CharField(max_length=255, choices=MEMBERSHIP_DURATION_CHOICES, default=MEMBERSHIP_DURATION_MONTHLY)
  agree_terms_condition = models.BooleanField(default=False)
  membership_receipt  = models.FileField(null=True, blank=True)
  
  
class SubscriptionPlan(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  
  
class UserContact(models.Model):
  name = models.CharField(max_length=255,blank=True, null=True)
  email = models.EmailField(blank=True, null=True)
  subject = models.CharField(max_length=255,null=True,blank=True)
  message = models.TextField(max_length=True,null=True)
  