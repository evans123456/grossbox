from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    food_business = User.objects.filter(groups__name='FoodBusiness')
    Service_Business = User.objects.filter(groups__name='ServiceBusiness')
    Customer = User.objects.filter(groups__name='	Customer')
    biker = User.objects.filter(groups__name='Biker')
    users = User.objects.all()
    
    context = {
        'number_of_foodbusiness':len(food_business),
        'number_of_Service_Business':len(Service_Business),
        'number_of_Customers': len(Customer),
        'number_of_bikers': len(biker),
        'users':users
    }
    return render(request,'s_admin/index.html',context)

def profile(request):
    return render(request,'s_admin/profile.html')