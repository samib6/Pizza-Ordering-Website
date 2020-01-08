from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        username = request.POST['username']
        Email = request.POST['Email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check password
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=Email).exists():
                    messages.error(request,'That email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,
                    email=Email,first_name=fname)

                    user.save()
                    messages.success(request,'You are now successfully registered')
                    return redirect('login')


        else:
            messages.error(request,'incorrect passwords')
            return redirect('register')
    else:

        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are now logged in')
            return redirect('pages:index')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now Logged out')
        return redirect('pages:index')
