from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import BOOK
from django.contrib import messages
from .models import isseuBook
from home.models import myUser 
from student.models import bookRequest
from datetime import date

# Create your views here.

#add book
@login_required
def add_book(request):
    if request.user.userType!='teacher':
        return redirect('/')
    if request.method=='POST':
        name=request.POST['bookName']
        author=request.POST['author']
        genre=request.POST['genre']
        if len(name)>2 and len(author)>=2 and genre!="":
            book=BOOK(name=name,author=author,genre=genre)
            book.save()
            messages.success(request, "book has been successfully added")
        else:
            messages.error(request, "Please fill the form correctly")
    books=BOOK.objects.all()
    param={'books':books}
    return render(request,'teacher/index.html',param)

#delete a book
@login_required
def delete_book(request,book_id):
    if request.user.userType!='teacher':
        return redirect('/')
    book=BOOK.objects.get(pk=book_id)
    # print(book)
    book.delete()
    messages.success(request,"Book has been deleted successfully")
    return redirect('add_book')

@login_required
def students(request):
    if request.user.userType!='teacher':
        return redirect('/')
    users=myUser.objects.all()
    param={'users':users}
    total_students=myUser.objects.filter(userType='student').filter(is_superuser=False).count()
    param['total_students']=total_students
    param['issuedbooks']=isseuBook.objects.all()
    return render(request,'teacher/students.html',param)

@login_required
def requests(request):
    if request.user.userType!='teacher':
        return redirect('/')
    bookRequests=bookRequest.objects.all()
    # print(bookRequests)
    param={'bookRequests':bookRequests}
    if request.method=='POST':
        response=request.POST['response']
        req_id=request.POST["request_id"]
        req=bookRequest.objects.get(request_id=req_id)
        if response=='accept':
            returndate=request.POST["returndate"]
            user=myUser.objects.filter(id=req.user.id)
            if req.type=='extend':
                # issueId=int()
                issue=isseuBook.objects.get(issue_id=req.issue_id)
                issue.return_date=returndate
                issue.save()
                # issue=isseuBook.objects.get(issue_id=issueId)
                
            else:
                issue=isseuBook.objects.create(user=user.first(),book=req.book,return_date=returndate,issue_date=date.today())
                issue.save()
            book=BOOK.objects.get (book_id=req.book.book_id)
            book.status='not available'
            req.delete()            
            book.save()
            messages.success(request, "book successfully issued")
        else:
            req.response='decline'
            req.save()
            messages.error(request, "book request has been declined")

    return render(request,'teacher/requests.html',param)

@login_required
def issuedBooks(request):
    if request.user.userType!='teacher':
        return redirect('/')
    iBooks=isseuBook.objects.all()
    param={'iBooks':iBooks}
    return render(request,'teacher/issuedBooks.html',param)