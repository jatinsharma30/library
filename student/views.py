from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from home.models import BOOK,myUser
from .models import bookRequest
from teacher.models import isseuBook


# Create your views here.
@login_required
def index(request):
    if request.user.userType!='student':
        return redirect('/')
    books=BOOK.objects.all()
    param={'books':books}
    return render(request,'student/index.html',param)

@login_required
def wishList(request):
    if request.user.userType!='student':
        return redirect('/')
    user=myUser.objects.filter(username="try3@gmail.com")
    book_requests=bookRequest.objects.filter(user=request.user)
    return render(request,'student/wishlist.html',{'user':user,'book_requests':book_requests})

@login_required
def requestBook(request):
    if request.user.userType!='student':
        return redirect('/')
    if request.method=='POST':
        name=request.POST['book']
        print('name is',name)
        print(request.user)
        book=BOOK.objects.filter(pk=name)
        print(book)
        if book[0].status=='not available':
            messages.danger(request,'This has been issued to another student')
        else:
            r=bookRequest.objects.filter(user=request.user).filter(book=book.first())
            if r.count()>0:
                messages.error(request,'request for this book has already been sent')
            else:
                r=bookRequest(user=request.user,book=book.first())
                #type='pending',response='pending'
                r.save()
                messages.success(request,'Your request has been sent successfully')
        return redirect('/student/wishList/')
    return HttpResponse('ok')

@login_required
def deleteRequest(request):
    if request.user.userType!='student':
        return redirect('/')
    if request.method=='POST':
        request_id=request.POST['request_id']
        req=bookRequest.objects.filter(request_id=request_id)
        req.delete()
        return redirect('/student/wishList/')

@login_required
def profile(request):
    if request.user.userType!='student':
        return redirect('/')
    id=request.user.id
    issued_books=isseuBook.objects.filter(user=id)
    c=0
    for book in issued_books:
        c+=int(book.calculate_fine())
    print(c)
    param={'books':issued_books,'total_fine':c}
    return render(request,'student/profile.html',param)

@login_required
def issued(request):
    if request.user.userType!='student':
        return redirect('/')
    iBooks=isseuBook.objects.filter(user=request.user)
    book_requests=bookRequest.objects.filter(user=request.user)
    param={'iBooks':iBooks,'book_requests':book_requests}
    return render(request,'student/issued_books.html',param)

@login_required
def extendDate(request):
    if request.user.userType!='student':
        return redirect('/')
    if request.method=='POST':
        issue_id=request.POST['issue_id']
        iBook=isseuBook.objects.filter(issue_id=issue_id)
        r=bookRequest(user=request.user,book=iBook.first().book,type='extend',issue_id=issue_id)
        r.save()
        messages.success(request,'Your request has been sent successfully')
    return redirect('/student/issued')

@login_required
def returnBook(request):
    if request.user.userType!='student':
        return redirect('/')
    if request.method=='POST':
        issue_id=request.POST['issue_id']
        iBook=isseuBook.objects.filter(issue_id=issue_id)
        book=BOOK.objects.get(book_id=iBook.first().book.book_id)
        book.status='available'
        book.save()
        iBook.delete()
        messages.success(request,'Your book has been returned')
    return redirect('/student/issued')