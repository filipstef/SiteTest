from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

rooms = [ 
    {'id':1, 'name':'Lets learn python'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Front-end developers'},
]

def test(request):
    return render(request,'main.html')

def home(request):
    context = {'rooms' : rooms}
    return render(request,'home.html', context)

def room(request):
    return render(request,'room.html')