from django.urls import path,include
from .views import  streamView
# from django.conf.urls.static import static
# from django.conf import settings


urlpatterns=[
    path('',streamView,name='streams'),

]