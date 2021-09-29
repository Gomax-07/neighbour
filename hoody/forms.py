from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *


class NeighborhoodModelForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = (
            'name',
            'location',
            'occupantsCount',
        )


class NeighborhoodForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField()
    occupantsCount = forms.IntegerField(min_value=0)


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'neighborhood',
            'email',
        )


class UserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

