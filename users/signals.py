from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import post_save, post_delete

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

@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# post_save.connect(create_profile, sender=User)
# post_delete.connect(delete_profile, sender=Profile)
