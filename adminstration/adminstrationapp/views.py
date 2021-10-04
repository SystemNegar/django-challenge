from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from werkzeug import Response
import json
from django.http import HttpResponse


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(1)
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return HttpResponse(json.dumps({"data": "User added"}))        

        print(2)
        print(form.errors)
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return HttpResponse(json.dumps({"errors": form.errors}),status=400)
    return HttpResponse(json.dumps({"data": "User added"}))

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return HttpResponse(json.dumps({"data": "User logged in"}))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return HttpResponse(json.dumps({"data": "User logged in"}))
