from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from . import forms

# Create your views here.
def index(request):
    pass

def registerbusiness(request):
    print('here')
    if request.method =='POST':
        form = forms.BusinessRegistrationForm(request.POST)
        print('post')
        if form.is_valid():
            print('form is valid')
            
            form.save()
            print('form saved')
            return redirect('/account')
    else:
        form = forms.BusinessRegistrationForm()
    context = {
        'form':form,
        'type': 'Business'
    }
    return render(request,'accounts/register.html',context)




def registerFoodbusiness(request):
    if request.method =='POST':
        form = forms.FoodbusinessRegistrationForm(request.POST)
        print('post')
        if form.is_valid():
            print('form is valid')
            user = form.save(commit=False)
            g = Group.objects.get(name="FoodBusiness")
            g.save()
            user.save()
            g.user_set.add(user)
            form.save()
            print('form saved')
            return redirect('/account')
    else:
        form = forms.FoodbusinessRegistrationForm()
    context = {
        'form':form,
        'type': 'Food Business'
    }
    return render(request,'accounts/register.html',context)


def registerLaborbusiness(request):
    if request.method =='POST':
        form = forms.LaborbusinessRegistrationForm(request.POST)
        print('post')
        if form.is_valid():
            print('form is valid')
            user = form.save(commit=False)
            g = Group.objects.get(name="ServiceBusiness")
            g.save()
            user.save()
            g.user_set.add(user)
            form.save()
            print('form saved')
            return redirect('/account')
    else:
        form = forms.LaborbusinessRegistrationForm()
    context = {
        'form':form,
        'type': 'Service Business'
    }
    return render(request,'accounts/register.html',context)
    

def registerbiker(request):
    if request.method =='POST':
        form = forms.BikerRegistrationForm(request.POST)
        print('post')
        if form.is_valid():
            print('form is valid')
            user = form.save(commit=False)
            g = Group.objects.get(name="Biker")
            g.save()
            user.save()
            g.user_set.add(user)
            form.save()
            print('form saved')
            return redirect('/account')
    else:
        form = forms.BikerRegistrationForm()
    context = {
        'form':form,
        'type': 'Biker'
    }
    return render(request,'accounts/register.html',context)