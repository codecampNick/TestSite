from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index_pageone.html', { 'title': 'PageOne Home' })
