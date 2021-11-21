from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.add_book,name='add_book'),
    path('delete_book/<book_id>',views.delete_book,name="delete_book"),
    path('students/',views.students,name='students'),
    path('requests/',views.requests,name='requests'),
    path('issuedBooks/',views.issuedBooks,name='issuedBooks'),
]
