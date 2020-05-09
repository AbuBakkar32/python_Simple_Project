from django.http import HttpResponse
from django.shortcuts import render

from first_app.models import BlogPost


def index(request):
    data = BlogPost.objects.all()
    return render(request, 'index.html', {'blog': data})
