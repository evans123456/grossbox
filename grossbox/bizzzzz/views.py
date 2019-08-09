from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'bizzzzz/index.html')

def list_of_business(request):
    # return render(request, '')
    pass