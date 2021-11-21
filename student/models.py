from django.db import models
from django.contrib.auth.models import User
from home.models import myUser,BOOK
# Create your models here.
class bookRequest(models.Model):
    request_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(myUser,null=True,on_delete=models.CASCADE)
    book=models.ForeignKey(BOOK,null=True,on_delete=models.CASCADE)
    types=[
        ('issue','issue'),
        ('extend','extend')
    ]
    type=models.CharField(max_length=6,choices=types,default='issue')
    responses=[
        ('accept','accept'),
        ('pending','pending'),
        ('decline','decline')
    ]
    response=models.CharField(max_length=7,choices=responses,default='pending')
    issue_id=models.CharField(max_length=100, default='')
    def __str__(self):
        return self.book.name + " to " + self.user.username
