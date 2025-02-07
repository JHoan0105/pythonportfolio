from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm #prebuilt form form django
from .forms import RegisterForm
from django.db import transaction


# Create your views here.
def register(request):
    if request.method == "POST":
        #form = UserCreationForm()
        form = RegisterForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            print(request.POST)
            return redirect("/home")
        elif not form.is_valid():
            print('Error completing form.')
            print(request.POST)
            print(form.errors)
            print(form.error_messages)
            print(form.password1, form.password2)
            return render(request, "register/register.html", {"form":form}) 
        else:
            print(form)
            print(form.cleaned_data)
            print(request.POST)
            print('failed to register')
            instance = form.save(commit=False)
            print(instance)
    else:
        # form = UserCreationForm()
        form = RegisterForm()
        # form reference here is used on the HTML
        print("failed to register")
        return render(request, "register/register.html", {"form":form})