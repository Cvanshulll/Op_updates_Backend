from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
import django.db.models.signals as signals
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from base.emails import send_account_activation_mail

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_mail_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile', blank=True, null=True)



@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            email = instance.email
            send_account_activation_mail(email, email_token)

    except Exception as e:
            print(e)