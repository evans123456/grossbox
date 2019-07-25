from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    pass

def register(request):
    if request.method =='POST':
        form = forms.FoodbusinessRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = forms.FoodbusinessRegistrationForm()
    
    context = {
        'form':form
    }

    return render(request,'accounts/register.html',context)
    