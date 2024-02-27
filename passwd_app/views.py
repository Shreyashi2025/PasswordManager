from django.shortcuts import render, redirect
from .models import Passwd_Manager
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .forms import ManageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

User = get_user_model()
def register(request):      #Registration
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('log_in')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,"reg.html",context)

def log_in(request):        #Login
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid Username or Password")
            return redirect('log_in')
    else:
        return render(request,"login.html")

def log_out(request):       #logout
    logout(request)
    return redirect('log_in')
#-----------------------CRUD-------------------------------
def home(request):
    if request.user.is_authenticated:
        manage = Passwd_Manager.objects.filter(user=request.user).order_by("-site_name")
        if request.method == "POST":
            passwd = 'PASSWORD_HERE'
            form = ManageForm(request.POST)
            form.passwd = make_password(passwd)
            if form.is_valid():
                new_manage = form.save()
                new_manage.user = request.user
                new_manage.save()
                return redirect('home')
        else:
            form = ManageForm()
        context ={"forms":form,"list":manage,"title":"Password Manager"}
        return render(request,'home.html',context)
    else:
        return redirect('log_in')

def edit(request,manage_id):
    manage = Passwd_Manager.objects.get(id=manage_id)
    if request.method == "POST":
        form = ManageForm(request.POST,instance=manage)
        if form.is_valid():
            form.save()
            messages.info(request,"List Updated!!!")
            return redirect('home')
    else:
        form = ManageForm(instance=manage)
    context ={"forms":form}
    return render(request,"edit.html",context)

def delete(request,manage_id):
    manage = Passwd_Manager.objects.get(id=manage_id)
    manage.delete()
    messages.info(request,"Item Removed!!!")
    return redirect('home')