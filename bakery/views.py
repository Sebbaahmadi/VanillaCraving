from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactForm

# Create your views here.
def home(request):

    return render (request,'pages/HOME.html')

def contactus (request):
    if request.method=='POST':
     #1 get data from form:
      v_name= request.POST.get('name')
      v_email= request.POST.get('e-mail')
      v_msg= request.POST.get('comments')
      #2 send data to DB
      v_contact = ContactForm(name= v_name, mail= v_email, text=v_msg)
      v_contact.save()
      return render (request,'pages/thank.html')
    else:
     return render(request,'pages/contactus.html')
    
def aboutus(request):
    return render(request,'pages/aboutus.html') 