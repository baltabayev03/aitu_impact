from django.shortcuts import render
from django.http import HttpResponse
import random

from .models import *

items1 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items2 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items3 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items4 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items5 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items6 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items7 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items8 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items9 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
items10 = ['static/Mainpage/img/sub1.png', 'static/Mainpage/img/sub2.png', 'static/Mainpage/img/sub3.png']
teachers = ['static/Mainpage/img/t1.png', 'static/Mainpage/img/t2.png', 'static/Mainpage/img/t3.png']


def index(request):
    characters = Characters.objects.all()
    return render(request, 'Characters/Characters.html', {'Characters':characters, 'title':Characters})
def index2(request):
    inventory = Inventory.objects.all()
    return render(request, 'Characters/Inventory.html', {'Inventory':inventory, 'title':Inventory})
def index3(request):
    donate = Donate.objects.all()
    return render(request, 'Donate/donate.html', {'Donate':donate, 'title':Donate})
def index4(request):
    signup = Signup.objects.all()
    return render(request, 'Signup/index.html', {'Signup':signup, 'title':Signup})

def indexx(request):
	return render(request, 'Mainpage/index.html')


def wish(request):
	return render(request, 'Mainpage/wish.html')


def items(request):
	# dictionary comprehension
	return render(request, 'Mainpage/items.html', {'teacher':random.choice(teachers), 'items1':random.choice(items1), 'items2':random.choice(items2), 'items3':random.choice(items3), 'items4':random.choice(items4), 'items5':random.choice(items5), 'items6':random.choice(items6), 'items7':random.choice(items7), 'items8':random.choice(items8), 'items9':random.choice(items9), 'items10':random.choice(items10)})


