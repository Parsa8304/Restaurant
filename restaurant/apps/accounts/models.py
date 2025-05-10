from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager


class UserManager(BaseUserManager):
       def create_user(self,email, user_name, password=None, **kwargs):
              if not email:
                     raise ValueError('Users must have an email address')
              if not user_name:
                     raise ValueError('Users must have a user name')             
              
              user = self.model(
                     email=self.normalize_email(kwargs.get('email')),
                     user_name=kwargs.get('user_name'),
                     first_name=kwargs.get('first_name', ''),
                     last_name=kwargs.get('last_name', ''),
              ) 
  
              
              user.save(using=self._db)
              return user

       def create_superuser(self, email, user_name, password=None, first_name=None, last_name=None):
              user = self.create_user(
                     email = self.normalize_email(email),
                     user_name = user_name,
                     password = password,
                     first_name = first_name,
                     last_name = last_name,
              )
              user.is_admin = True
              user.is_active = True
              user.is_staff = True
              user.is_superadmin = True
              user.save(using=self._db)
              return user

              
class User(AbstractUser):
       RESTAURANT = 'restaurant'
       CUSTOMER = 'customer'
       ADMIN = 'admin'
       ROLE_CHOICES = [
              (RESTAURANT, 'Restaurant'),
              (CUSTOMER, 'Customer'),
              (ADMIN, 'Admin'),
       ]
       
       first_name = models.CharField(max_length=30)
       last_name = models.CharField(max_length=30)
       username = models.CharField(max_length=30, unique=True)
       email = models.EmailField(max_length= 70,unique=True)
       phone_number = models.CharField(max_length=15, blank=True)
       role =models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
       
       #required fields
       date_joined = models.DateTimeField(auto_now_add=True)
       last_login = models.DateTimeField(auto_now_add=True)
       created_at = models.DateTimeField(auto_now_add=True)
       modified_at = models.DateTimeField(auto_now=True)
       is_admin = models.BooleanField(default=False)
       is_active = models.BooleanField(default=True)
       is_staff = models.BooleanField(default=False)
       is_superadmin = models.BooleanField(default=False)
       
       
       USERNAME_FIELD = 'email'
       REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
       
       def __str__(self):
              return self.username
       
       def has_perm(self, perm, obj=None):
              if self.is_superadmin:
                     return True
              return self.is_admin or self.is_staff
       
       def has_module_perms(self, app_label):
              return True

       
class UserProfile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
       profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
       cover_picture = models.ImageField(upload_to='cover_pictures/', blank=True, null=True)
       adress_line1 = models.CharField(max_length=255, blank=True, null=True)
       adress_line2 = models.CharField(max_length=255, blank=True, null=True)
       country = models.CharField(max_length=100, blank=True, null=True)
       city = models.CharField(max_length=100, blank=True, null=True)
       pin_code = models.CharField(max_length=20, blank=True, null=True)
       latitude = models.CharField(max_length=20, blank=True, null=True)
       longitude = models.CharField(max_length=20, blank=True, null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       modified_at = models.DateTimeField(auto_now=True)
       
       def __str__(self):
              return f"{self.user.username}'s Profile"

