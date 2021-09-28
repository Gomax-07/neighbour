from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *

User = get_user_model()


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



