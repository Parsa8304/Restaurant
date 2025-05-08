from django.db import models
from accounts.models import User, UserProfile


class Vendor(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile', null=False)
       user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='vendor_profile')
       vendor_name = models.CharField(max_length=255, unique=True)
       vendor_liecense = models.FileField(upload_to='vendor/liecense', unique=True)
       is_approved = models.BooleanField(default=False)
       created_at = models.DateTimeField(auto_now_add=True)
       modified_at = models.DateTimeField(auto_now=True)
       
       
       def __str__(self):
              return self.vendor_name
       
       