from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import random

# Create your views here.

def home(requests):
    return render(requests,'home.html')


def Pass_GenR(requests):
    char=list('abcdefghijklmnopqrstuvwxyz')

    if requests.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if requests.GET.get('digit'):
        char.extend(list('0123456789'))
    if requests.GET.get('symbol'):
        char.extend(list('!@#$%^&*~'))
    
    length=int(requests.GET.get('length',10))
    password=""
    for X in range(length):
        password+=random.choice(char)
    
    return render(requests,'pass.html',{'password':password})