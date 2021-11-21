from django.db import models
from django.contrib.auth.models import User
from datetime import date
from home.models import BOOK,myUser

class isseuBook(models.Model):
    
    issue_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(myUser,null=True,on_delete=models.CASCADE)
    book=models.ForeignKey(BOOK,null=True,on_delete=models.CASCADE)
    issue_date=models.DateField()
    return_date=models.DateField()
    # fine=models.DecimalField(max_digits=100,decimal_places=2,default=0)
    def __str__(self):
        return self.book.name + " to " + self.user.username

    def calculate_fine(self):
        fine=0
        if date.today() > self.return_date:
            fine=date.today() - self.return_date
            fine=str(fine).split(',')[0]
            fine=str(fine).split(' ')[0]
            # fine=str(fine).split(' ')
            
        return fine

