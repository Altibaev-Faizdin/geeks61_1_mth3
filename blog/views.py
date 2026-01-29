from django.shortcuts import render
from django.http import HttpResponse


def helo_world_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, World!")