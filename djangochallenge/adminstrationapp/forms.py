from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SeatManager, Stadium, Match
from django.forms import ModelForm


# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_superuser = False
        if commit:
            user.save()
        return user


class StadiumForm(ModelForm):
    class Meta:
        model = Stadium
        fields = ("name", "capacity", "city")


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ("stadium","teams", "match_date", "match_length")


class SeatManagerForm(ModelForm):
    class Meta:
        model = SeatManager
        fields = ('match', 'team_name', 'seat_range')