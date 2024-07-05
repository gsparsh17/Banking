from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    phoneNo=models.CharField(max_length=122)
    state=models.CharField(max_length=122)
    pincode=models.CharField(max_length=122)
    CustID=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    
    def __str__(self):
        return self.firstname

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User)
    