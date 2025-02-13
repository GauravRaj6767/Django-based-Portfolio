from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'portfolio_app/home.html')


def about(request):
    return render(request, 'portfolio_app/about.html')


def certifications(request):
    return render(request, 'portfolio_app/certifications.html')


def projects(request):
    return render(request, 'portfolio_app/projects.html')
