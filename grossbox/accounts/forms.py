from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bizzzzz import models as bizmodel

class FoodbusinessRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = bizmodel.Foodbusiness
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'manager_name',
            'id_number',
            'residence',
            'mobile',
            'biashara'
        )
    def save(self, commit=True):
        user = super(FoodbusinessRegistrationForm, self).save(commit=False)
        user.first_name = cleaned_data['first_name']
        user.last_name = cleaned_data['last_name']
        user.email = cleaned_data['email']

        if commit:
            user.save()
        
        return user