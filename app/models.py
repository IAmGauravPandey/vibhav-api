from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=13,default='')
    name=models.CharField(max_length=100,default='')
    branch=models.CharField(max_length=100,default='')
    coins=models.IntegerField(default=500)

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
         user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class Event(models.Model):
    name=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name

class EventRules(models.Model):
    event=models.OneToOneField(Event,on_delete=models.CASCADE)
    about=models.CharField(max_length=1500,default='')
    rules=models.CharField(max_length=1500,default='')
    judging=models.CharField(max_length=1500,default='')
    prizes=models.CharField(max_length=1500,default='')
    contacts=models.CharField(max_length=1500,default='')

    def __str__(self):
        return self.event.name

def create_rules(sender,**kwargs):
    if kwargs['created']:
         event_rules=EventRules.objects.create(event=kwargs['instance'])

post_save.connect(create_rules,sender=Event)

class Registration(models.Model):
    event=models.CharField(max_length=100,default='')
    team_name=models.CharField(max_length=50,default='')
    user=models.CharField(max_length=100,default='')
    token=models.CharField(max_length=20,default='0')

    

class UserToken(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    event1=models.CharField(max_length=20,default='0')
    event2=models.CharField(max_length=20,default='0')
    event3=models.CharField(max_length=20,default='0')
    event3=models.CharField(max_length=20,default='0')
    event4=models.CharField(max_length=20,default='0')
    event5=models.CharField(max_length=20,default='0')
    event6=models.CharField(max_length=20,default='0')
    event7=models.CharField(max_length=20,default='0')
    event8=models.CharField(max_length=20,default='0')
    event9=models.CharField(max_length=20,default='0')
    event10=models.CharField(max_length=20,default='0')
    event11=models.CharField(max_length=20,default='0')
    event12=models.CharField(max_length=20,default='0')
    event13=models.CharField(max_length=20,default='0')
    event14=models.CharField(max_length=20,default='0')

    def __str__(self):
        return self.user.username

def create_token(sender,**kwargs):
    if kwargs['created']:
         user_token=UserToken.objects.create(user=kwargs['instance'])

post_save.connect(create_token,sender=User)