from . import views

from django.urls import path

urlpatterns = [
    #path('الاسم اللي اليوزر يدور بيه', views.nameOftheView,name='')
    path('', views.home,name='HOME'),
    path('aboutus', views.aboutus, name='ABOUT US'),
    path('contactus',views.contactus,name='CONTACT US'),
    
]