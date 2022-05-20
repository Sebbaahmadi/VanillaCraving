from django.urls import path
from .import views

urlpatterns = [
path('BLOG',views.BLOG,name='BLOG')
]