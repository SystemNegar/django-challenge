from django import forms
from django.contrib.auth.models import User
from .forms import UserSeatForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import json
from django.http import HttpResponse
from adminstrationapp.models import SeatManager, Match
from .models import UserSeat


def reserve_seat(request):
    if request.method == "POST":
        user = request.user
        
        data = {
            'match': request.POST['match'],
            "user":user ,
            "team_name": request.POST['team_name']
            
        }
        form = UserSeatForm(data)
        if form.is_valid():
            seat_no = 0
            match_id = request.POST['match']
            team_name = request.POST['team_name']
            seat_query = SeatManager.objects.filter(match=match_id).filter(team_name=team_name).first()
            last_no = seat_query.last_seat_number
            
            if int(seat_query.seat_range.split('_')[0]) < int(last_no) < int(seat_query.seat_range.split('_')[1]):
                seat_no = int(last_no) + 1

            match_query = Match.objects.get(id=match_id)
            user_seat_obj = UserSeat(match=match_query, team_name=team_name, seat_no=seat_no, user=user)
            user_seat_obj.save()
            seat_query.last_seat_number = int(seat_query.last_seat_number) + 1
            seat_query.save()
            return HttpResponse(json.dumps({"data": {
                'id': user_seat_obj.id,
                'seat_number': user_seat_obj.seat_no,
                'team_name': user_seat_obj.team_name
            }}))        

        messages.error(request, "Unsuccessful registration. Invalid information.")
        return HttpResponse(json.dumps({"errors": form.errors}),status=400)

    return HttpResponse(json.dumps({"data": "Seat added"}))