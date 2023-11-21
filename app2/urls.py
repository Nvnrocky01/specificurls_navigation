from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('bhavani/',bhavani,name='bhavani')
]