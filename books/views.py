from django.shortcuts import render,redirect
from .models import Contact
from books.forms import SaveConatct
from django.http import HttpResponse
from .models import Book

def index(request):
    books=Book.objects
    return render(request,"index.html",{'books':books})


def aboutus(request):
    return render(request,"about.html")

def contactus(request):
    contacts=Contact.objects
    if request.method=='POST':
        form=SaveConatct(request.POST or None)
        if form.is_valid():
            form.save
    return render(request,"contact.html",{'contacts':contacts})

def delete(request,contact_id):
    contact=Contact.objects.get(pk=contact_id)
    contact.delete()
    return render(request,'contact.html')


def edit(request,contact_id):
    if request.method=='POST':
        contact=Contact.objects.get(pk=contact_id)
        form=SaveConatct(request.POST or None,instance=contact)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        contact=Contact.objects.get(pk=contact_id)
        return render(request,'edit.html',{'contact':contact})