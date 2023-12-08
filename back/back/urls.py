"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.template.backends import django
from django.templatetags.static import static

from django.urls import path, include
from django.views.generic import RedirectView

from back.uinfo import views
from back.uinfo.views import *

urlpatterns = [

    path('appointment/', include('appointment.urls')),
    # path('', views.index, name='home'),

    #message urls
    path(r'messages/', include('django_messages.urls')),

    path('admin/', admin.site.urls),

    path('psyholog', views.psyho, name="Psyho"),

    path('client', views.client, name="Client"),

    #path('', views.clinic, name="Homepage"),
    path('', LoginUser.as_view(), name="Authorization"),
    path('logout/', logout_user, name='logout'),
    path('clinic', views.clinic, name="Clinic"),
    path('personpage', views.personpage, name="Personpage"),
    #path('personpage', PersonPage.as_view(), name="Personpage"),
    path('register', RegisterUser.as_view(), name="Register"),


    path('<int:pk>', PatientDetail.as_view(), name="patient_detail" ),
   # path('appointment', AppointmentInfo.as_view(), name="Appointment"),
    path('appointment_info', AppointmentListView.as_view(), name="Appointment_Info"),


    path('<int:pk>', UserInfo.as_view(), name="Userinfo"),
    path('myclients', ServiceListView.as_view(), name="Doctor"),

    path('mRecord', MRecordsListView.as_view(), name="MRecord"),

    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]