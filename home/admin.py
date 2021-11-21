from django.contrib import admin
from .models import BOOK, myUser
# Register your models here.
admin.site.register(BOOK)
admin.site.register(myUser)
# admin.site.register(extendUser)