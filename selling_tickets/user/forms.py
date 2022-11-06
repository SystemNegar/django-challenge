from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('mobile_number',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('mobile_number',)
