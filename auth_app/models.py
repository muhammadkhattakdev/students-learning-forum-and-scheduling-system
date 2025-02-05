from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Related User Model')

    def __str__(self):

        return self.user.first_name

class Student(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Related User Model')
    img = models.ImageField(upload_to='student_images', default='', null=True, verbose_name="Student Image")

    def __str__(self):

        return self.user.first_name


class Notification(models.Model):

    content = models.TextField(verbose_name="Content")
    read_by_users = models.ManyToManyField(to=User, verbose_name="Read by Users")


    def __str__(self):

        return self.content


