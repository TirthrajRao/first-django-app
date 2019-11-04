from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib import messages
from .models import Posts
from .models import Feedback
# from .forms import signUpForm



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
                messages.info(request,'Username Already Exists')
                return redirect ('signup')
            elif User.objects.filter(email=email).exists():
                print ('Email taken')
                messages.info(request,'Email Already Exists')
                return redirect ('signup')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                res = send_mail("Thanks For Registering With Us", "Enjoy Trivia Post", "noreplay@triviapost.com", [email])
                print('user created successfully!!!')
                return redirect ('login')
        else:
            print('Password not matching!!!')
            messages.info(request,'Password Not Matching')
            return redirect ('signup')
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

    if request.user.is_authenticated:
        posts  = Posts.objects.all() 
        return render(request, "post.html",{'posts':posts})
    else:
        return redirect ('login')

def logout(request):

    auth.logout(request)
    return redirect ('index')

def feedback(request):

    if  request.method == 'POST':
        
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']

        feedback = Feedback(email=email,mobile=mobile,message=message)
        feedback.save()
        print('feedback submitted successfully!!!')
        messages.info(request,'feedback submitted successfully')
        return redirect ('feedback')    
    else:
         return render(request, "feedback.html")

def feedbackList(request):

    if request.user.is_authenticated:
        feedback  = Feedback.objects.all() 
        return render(request, "feedbackList.html",{'feedback':feedback})
    else:
        return redirect ('login')


