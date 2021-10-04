from django import forms
from .models import UserSeat
from django.forms import ModelForm
from adminstrationapp.models import SeatManager


# Create your forms here.


class UserSeatForm(ModelForm):
    class Meta:
        model = UserSeat
        fields = ("user", "match", "team_name")

