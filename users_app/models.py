from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

def user_directory_path(instance, filename):
    """ Generate uploaded file path to MEDIA_ROOT/user_<id>/<filename>"""

    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    """ Extend User model with profile """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=user_directory_path)

    def save(self, *args, **kwargs):
        """ Delete old avatar before save a new one """

        update_fields=None
        try:
            this = Profile.objects.get(id=self.id)
            if this.avatar != self.avatar:
                os.remove(this.avatar.path)
            else:
                update_fields=["user", "about"]
        except: 
            pass
        super().save(update_fields=update_fields, *args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ Handle User model signal to create Profile model """
    
    if created:
        Profile.objects.create(user=instance)
