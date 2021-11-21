from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handleLogin,name='handleLogin'),
    path('logout',views.handleLogout,name='handleLogout'),
    # path('add_book',views.add_book,name="add_book"),
    # path('delete_book/<book_id>',views.delete_book,name="delete_book"),
    # path('show',views.show,name='show'),
]
