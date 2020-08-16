from django.views.generic import CreateView, FormView,UpdateView
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from .models import User,Notification
from .forms import UserSignupForm, UserLoginForm,ClientSignupForm,WriterSignupForm


class UserRegistrationCreateView(FormView):
    """
    Create user api view
    """
    model = User
    form_class = UserSignupForm
    template_name = 'authenticate/register.html'

    def post(self, request):
        """
        Overide the default post()
        """
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        data = {
            "first_name": form.cleaned_data['first_name'],
            "last_name": form.cleaned_data['last_name'],
            "username":form.cleaned_data['username'],
            "password": form.cleaned_data['password'],
            "email": form.cleaned_data['email'].lower(),
        }
        User.objects.create_user(**data)
        signup_user=User.objects.get(email=data['email'])
        # client_group=Group.objects.get(name='clients_group')
        # client_group.user_set.add(signup_user)
        return redirect(reverse('authentication:login'))

class ClientRegistrationCreateView(FormView):
    """
    Create user api view
    """
    model = User
    form_class =ClientSignupForm
    template_name = 'authenticate/register.html'

    def post(self, request):
        """
        Overide the default post()
        """
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        data = {
            "first_name": form.cleaned_data['first_name'],
            "last_name": form.cleaned_data['last_name'],
            "username":form.cleaned_data['username'],
            "password": form.cleaned_data['password'],
            "email": form.cleaned_data['email'].lower(),
            "date_of_birth": form.cleaned_data['date_of_birth'],
        }
        User.objects.create_user(**data)
        return redirect(reverse('authentication:login'))

class WriterRegistrationCreateView(FormView):
    """
    Create user api view
    """
    model = User
    form_class = WriterSignupForm
    template_name = 'authenticate/register.html'

    def post(self, request):
        """
        Overide the default post()
        """
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        data = {
            "first_name": form.cleaned_data['first_name'],
            "last_name": form.cleaned_data['last_name'],
            "username":form.cleaned_data['username'],
            "password": form.cleaned_data['password'],
            "email": form.cleaned_data['email'].lower(),
            "phone": form.cleaned_data['phone'],
            "additional_phone": form.cleaned_data['additional_phone'],
            "first_discipline": form.cleaned_data['first_discipline'],
            "second_discipline": form.cleaned_data['second_discipline'],
            "third_discipline": form.cleaned_data['third_discipline'],
            "fourth_discipline": form.cleaned_data['fourth_discipline'],
            "fifth_discipline": form.cleaned_data['fifth_discipline'],
            "academic_degree": form.cleaned_data['academic_degree'],
            "time_zone": form.cleaned_data['time_zone'],
            "night_calls": form.cleaned_data['night_calls'],
        }
        User.objects.create_user(**data,is_staff=True)
        return redirect(reverse('authentication:login'))



class UserLoginCreateView(FormView):
    """
    Create user api view
    """
    model = User
    form_class = UserLoginForm
    template_name = 'authenticate/login.html'
    success_url = reverse_lazy("index")

    def post(self, request):
        """
        Overide the default post()
        # """
        form = self.form_class(request.POST)
        email = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user and user.is_active:
            login(request, user)
            return super(UserLoginCreateView, self).form_valid(form)
        messages.success(request, 'This email and password combination is invalid', extra_tags='red')
        return render(request, self.template_name, {"form": form})


def logout_view(request):
    logout(request)
    if request.user.is_superuser or request.user.is_staff:
        redirect('/accounts/login')
    else:
        return redirect('/')


def show_notification(request,notification_id):
    n=Notification.objects.get(id=notification_id)
    return render(request,'notification.html',{'notification':n})


def delete_notification(request,notification_id):
    n=Notification.objects.get(id=notification_id)
    n.viewed=True
    n.save()
    return redirect('/')


def profile_view(request):
    context={}
    context['user']=User.objects.get(id=request.user.id)
    return render(request,'profile.html',context)



