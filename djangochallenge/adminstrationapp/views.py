from django import forms
from django.contrib import auth
from django.shortcuts import render, redirect
from .forms import MatchForm, NewUserForm, SeatManagerForm, StadiumForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import json
from django.http import HttpResponse


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return HttpResponse(json.dumps({"data": "User added"}))        

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
            return HttpResponse(json.dumps({"data": form.errors}))

    return HttpResponse(json.dumps({"data": "User logged in"}))


def authentication(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps({
            'data': 'token is not valid'
        }), status=400)

    is_superuser = request.user.is_superuser
    if not is_superuser:
        return HttpResponse(json.dumps({
            'data': "permission denied"
        }), status=400)

def add_stadium(request):
    if request.method == "POST":
        authentication(request)

        form = StadiumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({
                'data': 'Stadium added'
            }))

        return HttpResponse(json.dumps({
            'errors': form.errors
        }), status=400)


def add_match(request):
    if request.method == 'POST':
        authentication(request)

        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps(
                {
                    'data': 'Match Added'
                }
            ))
        
        return HttpResponse(json.dumps({
            'error': form.errors
        }), status=400)


def add_seat(request):
    if request.method == 'POST':
        authentication(request)

        form = SeatManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps(
                {
                    'data': 'Seat Added'
                }
            ))
        
        return HttpResponse(json.dumps(
            {
                'errors': form.errors
            }
        ), status=400)