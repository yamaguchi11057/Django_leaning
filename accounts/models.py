from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """Expand User model"""
    class Meta:
        verbose_name_plural = 'CustomUser'