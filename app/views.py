from django.shortcuts import render
from .models import *
# from app.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('admin')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

@login_required
def home(request):
    if request.method == 'POST':
        try:
            file = request.FILES['file']
            user = UserProfileInfo(file=file)
            user.save()
        except:
            return HttpResponse('something went wrong')
        subject = 'Resume Uploaded Sucessfully'
        message = ' Thank you for your resume '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email,]
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponse(subject)
    return render(request,'home.html')