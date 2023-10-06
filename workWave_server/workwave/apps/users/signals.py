from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail 
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_email_verification(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Workwave!'
        message = f'Hello {instance.first_name}!\n\nWelcome to Workwave. Thank you for joining us.'
        from_email = 'from@yourdjangoapp.com'
        recipient_list = (instance.email,)
        send_mail(subject, message, from_email,recipient_list)
