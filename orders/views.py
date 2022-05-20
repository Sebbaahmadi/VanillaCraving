from django.shortcuts import render
from .models import product
# Create your views here.

def BLOG (request):
    post=product.objects.all()
    return render(request,'orders/orders.html',{'post':post})