from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

from .forms import *
from .models import *


# from .utils import *




class ServiceListView(ListView):
    model = TenantUser
    template_name = 'main/psyholog/myclients.html'
    queryset = TenantUser.objects.all().order_by('name')


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'main/appointment_info.html'
    queryset = Appointment.objects.all().order_by('medicalcard_id')


class MRecordsListView(ListView):
    model = MedicalCard
    template_name = 'main/medical_record.html'
    queryset = MedicalCard.objects.all().order_by('user_id')


def personpage(request):
    appointments = Appointment.objects.all()

    context = {
        'appointments': appointments,
    }
    return render(request, "main/personpage.html", context=context)


def clinic(request):
    return render(request, "main/start.html")


def home(request):
    return render(request, "main/home.html")


class UserInfo(UpdateView):
    model = TenantUser
    form_class = UserInfoForm
    template_name = 'main/userinfo.html'
    success_url = reverse_lazy("Personpage")


class AppointmentInfo(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'main/appointment.html'
    success_url = reverse_lazy("Appointment_Info")


class PatientDetail(DetailView):
    model = TenantUser
    template_name = 'main/details_view.html'
    context_object_name = 'patient'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy("Personpage")

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign up")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("Authorization")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/authorization.html'

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign in")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        #return reverse_lazy("Personpage")
        user = self.request.user
        if user.is_staff==False:
            return reverse_lazy('Client')
        elif user.is_staff==True:
            return reverse_lazy('Psyho')

        '''
        group_name=Group.objects.all().filter(user = self.request.user)# get logget user grouped name
        group_name=str(group_name[0]) # convert to string

        if "Client" == group_name:
            return reverse_lazy('Client')
        elif "Psyho" == group_name:
            return reverse_lazy('Psyho')
        '''

def psyho(request):
    return render(request, "main/psyholog/index.html")

def client(request):
    return render(request, "main/client/index.html")


def logout_user(request):
    logout(request)
    return redirect("Authorization")


def medical_record(request):
    return render(request, "main/medical_record.html")