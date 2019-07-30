from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bizzzzz import models as bizmodel
from bikers import models as bikemodel
from leaflet.forms.widgets import LeafletWidget
from django.contrib.gis.db import models
from leaflet.forms.fields import PointField





class BusinessRegistrationForm(forms.ModelForm):
    location = PointField()
    class Meta:
        model = bizmodel.Business
        fields = (
            'business_name',
            'mobile_number',
            'location',
        )
        widgets = {'location': LeafletWidget()}
    def save(self, commit=True):
        user = super(BusinessRegistrationForm, self).save(commit=False)
        user.business_name = self.cleaned_data['business_name']
        user.mobile_number = self.cleaned_data['mobile_number']
        user.location = self.cleaned_data['location']
        if commit:
            user.save()
        return user

class LaborbusinessRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = bizmodel.Laborbusiness
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
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


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
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class BikerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    area_of_business = PointField()
    class Meta:
        model = bikemodel.Biker
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'date_of_birth',
            'id_number',
            'residence',
            'mobile_number',
            'vehiecle',
            'area_of_business'
        )
        widgets = {'area_of_business': LeafletWidget()}
    def save(self, commit=True):
        user = super(FoodbusinessRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        user.id_number = self.cleaned_data['id_number']
        user.residence = self.cleaned_data['residence']
        user.mobile_number = self.cleaned_data['mobile_number']
        user.vehiecle = self.cleaned_data['vehiecle']
        user.area_of_business = self.cleaned_data['area_of_business']
        
        if commit:
            user.save()
        return user