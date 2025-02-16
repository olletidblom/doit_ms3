from django.db import models
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    fname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    bio = RichTextField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    birthdate = models.DateField(blank=True, null=True) 
    updated_at = models.DateTimeField(default=timezone.now) 
    def __str__(self):
        return f"{self.fname} {self.lname}" if self.fname and self.lname else self.user.username

    def save(self, *args, **kwargs):
        """Override save method to update `updated_at` field."""
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        Profile.objects.create(user=instance)