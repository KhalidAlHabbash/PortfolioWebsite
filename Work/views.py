from django.shortcuts import render
from .models import Job


def homepage(request):
    jobs = Job.objects
    return render(request, 'Work/home.html', {'jobs':jobs})
