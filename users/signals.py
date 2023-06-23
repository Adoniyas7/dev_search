from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email= user.email,
            name= user.first_name
        )
        subject="Welcome to DevSearch"
        message=f" Hi {profile.username}, thank you for joining DevSearch. We hope you enjoy our service. "
        

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
        )
        
@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# post_save.connect(create_profile, sender=User)
# post_delete.connect(delete_profile, sender=Profile)
