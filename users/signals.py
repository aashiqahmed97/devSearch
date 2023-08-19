from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import profile
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User) 
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profiles = profile.objects.create(
            user=user,
            email=user.email,
            name=user.first_name,
        )
        subject = 'Welcome to devSearch'
        message = 'We are glad you are here!'


        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently = False,

        )

@receiver(post_save, sender= profile) 
def updateUser(sender, instance, created, **kwargs):
    profile=instance
    user=profile.user


    if created == False:
        user.first_name = profile.name
        user.username = profile.userName  # Use 'userName' instead of 'username'
        user.email = profile.email
        user.save()







@receiver(post_delete, sender=User)
def deleteUser(sender, instance, **kwargs):
    print('Deleting user')




#post_save.connect(createProfile, sender=profile)   
#post_delete.connect(deleteUser,sender=profile)