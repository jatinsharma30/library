from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     is_student = models.BooleanField(default=True)
#     is_teacher = models.BooleanField(default=False)

# Create your models here.
class BOOK(models.Model):
    book_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    genres = [
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Fiction', 'Fiction'),
        ('Horror', 'Horror'),
        ('Mythology', 'Mythology'),
        ('Mystery','Mystery'),
        ('Science Fiction','Science Fiction')
    ]
    genre = models.CharField(
        max_length=15,
        choices=genres,
        default='Drama',
    )
    statusValue=[
        ('available','available'),
        ('not available','not available')
    ]
    status=models.CharField(max_length=13,choices=statusValue,default='available')
    def __str__(self):
        return self.name + " by " + self.author

    
class myUser(AbstractUser):
    userTypes=[
        ('teacher','teacher'),
        ('student','student')
    ]
    userType=models.CharField(
        max_length=7,
        choices=userTypes,
        default='student'
        )