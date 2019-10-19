from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib import messages
from .models import Posts



def index(request):
    return render(request, "index.html")

def signup(request):

    if  request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                print ('Email taken')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                res = send_mail("Thanks For Registering With Us", "Enjoy Trivia Post", "noreplay@triviapost.com", [email])
                print('user created successfully!!!')
                return HttpResponse('User Created Successfully!!!')
        else:
            print('Password not matching!!!')

    else:
         return render(request, "signup.html")

def editProfile(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        user = User.objects.filter(id=userId).update(first_name=first_name,last_name=last_name,username=username,email=email)
        user.save();
        print ('user updated successfully!!!')

def deleteUser(request):

    if request.method == 'DELETE':

        userId = request.POST['userId']
        user = User.objects.get(id=userId)
        user.delete()
        print('user deleted successfully!!!')
    else:
        print('Bad Request!!!')

def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect ('post')
        else:
            messages.info(request,'invalid credentials')
            return redirect ('login')

        print('Data',username,password)

        print('Inside POST Method')
    else:
        return render(request,"login.html")
        
def post(request):
    posts  = Posts.objects.all() 
    return render(request, "post.html",{'posts':posts})    