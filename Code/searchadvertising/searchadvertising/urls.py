"""searchadvertising URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from adagency.views import *
from searchadvertising.views import index, adminlogin, adminloginaction, logout, userdetails, activateuser, \
    adagencydetails, activateadagency, accuracy, adminhome
from user.views import user, userlogincheck, userregistration, adds, viewdetails, search, usersearchresult, userpage,adds1,viewadagency,frgt

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^index/', index, name="index"),
    url(r'^adminlogin/', adminlogin, name="adminlogin"),
    url(r'^adminhome/', adminhome, name="adminhome"),
    url(r'^adminloginaction/', adminloginaction, name="adminloginaction"),
    url(r'^userdetails/', userdetails, name="userdetails"),
    url(r'^activateuser/', activateuser, name="activateuser"),
    url(r'adagencydetails/', adagencydetails, name="adagencydetails"),
    url(r'^activateadagency/', activateadagency, name="activateadagency"),
    url(r'^accuracy/', accuracy, name="accuracy"),
    url(r'^logout/', logout, name="logout"),

    url(r'^user/', user, name="user"),
    url(r'^userlogincheck/', userlogincheck, name="userlogincheck"),
    url(r'^userregistration/', userregistration, name="userregistration"),
    url(r'^userpage/', userpage, name="userpage"),
    url(r'^adds/', adds, name="adds"),
    url(r'^adds1/', adds1, name="adds1"),
    url(r'^viewdetails/', viewdetails, name="viewdetails"),
    url(r'^search/', search, name="search"),
    url(r'^usersearchresult/', usersearchresult, name="usersearchresult"),
    #url(r'^useresucces/',useresucces, name="useresucces"),

    url(r'^adagency/', adagency, name="adagency"),
    url(r'^adagencylogincheck/', adagencylogincheck, name="adagencylogincheck"),
    url(r'^adagencyregistration/', adagencyregistration, name="adagencyregistration"),
    url(r'^adagencypage/', adagencypage, name="adagencypage"),
    url(r'^uploadadds/', uploadadds, name="uploadadds"),
    url(r'^viewadds/', viewadds, name="viewadds"),
    url(r'^viewadagency/',viewadagency,name='viewadagency'),
    url(r'^frgt/',frgt,name='frgt')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)