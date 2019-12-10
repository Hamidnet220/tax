from django.shortcuts import render,redirect
from django.contrib import auth

def register(request):
    return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('pages:home')
        else:
            return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html')

def logout(request):

    if request.method=='POST':
        auth.logout(request)
        return render(request,'pages/home.html')

def dashboard(request):
    return(request,'accounts/dashboard.html')
