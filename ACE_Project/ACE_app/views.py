from django.shortcuts import render
from ACE_app.models import Topic, User, Webpage, AccessRecord
from . import forms  
from ACE_app.forms import NewUserForm, UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse 
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here. Store functions to handle requests and return responses

def index(request):
    #context_dict = {'text':'hello world','number':100}
    return render(request,'ACE_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


def register(request):

    registered = False

    if request.method == "POST":
        #matches variable sent to template tagging
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password) #hashing the password
            user.save()

            profile = profile_form.save(commit=False) # avoid potential collisions the first time through
            profile.user = user # sets up the one-one relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'ACE_app/registration.html',{'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password= password) #Django's built-in authenticator

        if user:
            if user.is_active:
                login(request,user) #another built in
                return HttpResponseRedirect(reverse('index')) #will send back to home page if active
            else:
                return HttpResponse("Account not Active!")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'ACE_app/login.html',{})

def other(request):
    return render(request,'ACE_app/other.html')

def relative(request):
    return render(request,'ACE_app/relative_url_templates.html')

def form_name_view(request):
    form=forms.FormName()

    if request.method == "POST":
        form=forms.FormName(request.POST)

        if form.is_valid():
            #Do something
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])


    return render(request, 'ACE_app/form_page.html',{'form':form})


def help(request):
    help_dict = {'help_insert':"Help Page"}
    return render(request,'ACE_app/help.html',context=help_dict)

def users(request):
    form = NewUserForm()

    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM not valid")
    return render(request,'ACE_app/users.html',{'form':form})