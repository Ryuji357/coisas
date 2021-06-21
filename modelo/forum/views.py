from django.http import HttpResponse
from django.shortcuts import render

from .models import *

def index(request):
    context = {'teste': 'shflkjnvlkrej'}
    return render(request, 'forum/base.html', context)