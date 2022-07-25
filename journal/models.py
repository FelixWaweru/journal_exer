from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Database Models

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, first_name, last_name, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")
        if other_fields.get('is_active') is not True:
            raise ValueError("Superuser must have is_active=True")

        return self.create_user(first_name, last_name, email, password, **other_fields)


    def create_user(self, first_name, last_name, email, password, **other_fields):
        if not email:
            raise ValueError(_("Invalid email provided"))

        email = self.normalize_email(email)
        user = self.model(first_name = first_name, last_name = last_name, email = email, **other_fields)
        user.set_password(password)
        user.save()
        return user

# User Model
class Member(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    last_post = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # Default User Model import
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

# The Journal Entry Model
class Entry(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    text_post = models.CharField(max_length=500)
    entry_date = models.DateTimeField()
    share_status = models.BooleanField(default=False)

# The Shared Posts Model
class Share(models.Model):
    entry_id = models.ForeignKey(Entry,
                                    on_delete=models.CASCADE)
    shared_with = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    share_date = models.DateField()
