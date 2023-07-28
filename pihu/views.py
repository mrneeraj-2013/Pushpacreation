from django.shortcuts import render, HttpResponse
from datetime import datetime
from pihu.models import Contact
from django.contrib import messages

def index(request):
    context = {
        "variable": "",
        "variable": ""
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is home page")

def about(request):
    #messages.success(request,"This is about")  # this is use for aleart message show on about page.
    return render(request,'about.html')
    return HttpResponse("this is  about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is  services page")  

def contact(request):
    
    if request.method == "POST":  # this use for store contact data 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today)
        contact.save() # save data in database.
        messages.success(request, 'Thank You For Contact.') #this is aleart message when someone fill contact form.
    
    return render(request,'contact.html')
    #return HttpResponse("this is  contact page")

def career(request):
    return render(request,'career.html')
    #return HttpResponse("this is  career page")
#def Submit(request):
 #  return render(request,'Submit.html')
    #return HttpResponse("this is  career page")   /*** 