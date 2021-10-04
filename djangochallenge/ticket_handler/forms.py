from django import forms
from .models import UserSeat
from django.forms import ModelForm
from adminstrationapp.models import SeatManager


# Create your forms here.


class UserSeatForm(ModelForm):
    class Meta:
        model = UserSeat
        fields = ("user", "match", "team_name")

    def save(self, commit=True):
        seat = super(UserSeatForm, self).save(commit=False)
        seat_query = SeatManager.objects.filter(match=seat.match).filter(team_name=seat.team_name).first()
        last_no = seat_query.last_seat_number
        if int(last_no) < int(seat_query.seat_range.split('_')[1]):
            seat.seat_no = int(last_no) + 1
            seat.save()

        return seat
