from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('',views.index,name='index'),
    path('wishList/',views.wishList,name='wishList'),
    path('wishList/deleteRequest/',views.deleteRequest,name='deleteRequest'),
    path('request/',views.requestBook,name='requestBook'),
    path('profile/',views.profile,name='profile'),
    path('issued/',views.issued,name='issued'),
    path('issued/returnBook/',views.returnBook,name='returnBook'),
    path('issued/extendDate/',views.extendDate,name='extendDate'),
]
