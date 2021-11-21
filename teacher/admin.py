from django.contrib import admin
from .models import isseuBook

# Register your models here.
class issueBookAdminSite(admin.ModelAdmin):
    model=isseuBook
    fields=['user','book','issue_date','return_date']
    list_display=('user','book','calculate_fine')
admin.site.register(isseuBook,issueBookAdminSite)
