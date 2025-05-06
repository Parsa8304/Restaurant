from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile



@receiver(post_save, sender=User)       
def post_save_create_user_profile(sender, instance, created, **kwargs):
       if created:
              UserProfile.objects.create(user=instance)
       else:
              instance.profile.save()
              
# post_save.connect(post_save_create_user_profile, sender=User)
@receiver(pre_save, sender=UserProfile)
def pre_save_profile_reciver(sender, instance, **kwargs):
       print(f'{instance.user.username} profile is being saved')
       