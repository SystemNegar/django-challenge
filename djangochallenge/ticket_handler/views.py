from django import forms
from django.contrib.auth.models import User
from .forms import UserSeatForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import json
from django.http import HttpResponse


def reserve_seat(request):
    if request.method == "POST":
        user = request.user
        
        data = {
            'match': 1,
            "user":user ,
            "team_name": "firstteam"
            
        }
        form = UserSeatForm(data)
        if form.is_valid():
            seat = form.save()

            return HttpResponse(json.dumps({"data": "Seat Added"}))        

        messages.error(request, "Unsuccessful registration. Invalid information.")
        return HttpResponse(json.dumps({"errors": form.errors}),status=400)

    return HttpResponse(json.dumps({"data": "Seat added"}))