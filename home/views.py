from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages 
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import myUser
from home.models import BOOK
# from home.models import extendUser, CustomUser
from django.contrib.auth.decorators import login_required


# Create your views here.

#login page

#home page
def home(request):
    books=BOOK.objects.all()
    param={'books':books}
    return render(request,'home/home.html',param)

# def add_book(request):
#     if request.method=='POST':
#         name=request.POST['bookName']
#         author=request.POST['author']
#         genre=request.POST['genre']
#         if len(name)>2 and len(author)>2 and genre!="":
#             book=BOOK(name=name,author=author,genre=genre)
#             book.save()
#             messages.success(request, "book has been successfully added")
#         else:
#             messages.error(request, "Please fill the form correctly")
#     books=BOOK.objects.all()
#     param={'books':books}
#     return render(request,'home/addbook.html',param)

#delete a book
def delete_book(request,book_id):
    book=BOOK.objects.get(pk=book_id)
    print(book)
    book.delete()
    messages.success(request,"Book has been deleted successfully")
    return redirect('addbook')

def handleSignup(request):
    if request.method=='POST':
        # email=request.POST['signupEmail']
        username=request.POST['signupEmail']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password1=request.POST['sinupPassword']
        password2=request.POST['sinupPassword2']
        type=request.POST['type']
        print(fname,lname,password1,password2,type)
        if myUser.objects.filter(username=username).exists():
            messages.error(request,'username taken kindly login or enter another username')
            return redirect('/')
        else:
            myuser=myUser.objects.create_user(username=username,email=username ,password=password1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.userType=type
            myuser.save()
            if type=='teacher':
                auth.login(request,myuser)
                messages.success(request,'you account has been successfully created as teacher')
                return redirect('/teacher')
            else :
                auth.login(request,myuser)
                messages.success(request,'you account has been successfully created as student')
                return redirect('/student')
    else:
        return HttpResponse('404 page not found')

def handleLogin(request):
    if request.method=='POST':
        username=request.POST['loginEmail']
        password=request.POST['loginPassword']
        # to check 
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.userType=='student':
            auth.login(request,user)
            messages.success(request,'you logged in as student successfully')
            return redirect('/student')
        elif user is not None and user.userType=='teacher':
            auth.login(request,user)
            messages.success(request,'you logged in as teacher successfully')
            return redirect('/teacher')
        else:
            return HttpResponse('user does not exist')

    else:
        return HttpResponse('404 page not found')


def handleLogout(request):
    logout(request)
    return redirect('/')

# to check user infos
# @login_required(login_url='/home/')
# def show(request):
#     #request.user give current active user
#     data=User.objects.filter(username=request.user)
#     # data=User.objects.get(type=request.user)
#     for d in data:
#         print(d)
#     return HttpResponse(request,data)