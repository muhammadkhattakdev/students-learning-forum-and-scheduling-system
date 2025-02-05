from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Email Address')
    username = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    def __str__(self):
        return self.email


class Teacher(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, verbose_name='Related User Model')

    def __str__(self):

        return self.user.first_name

class Student(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, verbose_name='Related User Model')
    img = models.ImageField(upload_to='student_images', default='', null=True, verbose_name="Student Image")

    def __str__(self):

        return self.user.first_name


class Notification(models.Model):

    content = models.TextField(verbose_name="Content")
    read_by_users = models.ManyToManyField(to=CustomUser, verbose_name="Read by Users")


    def __str__(self):

        return self.content


