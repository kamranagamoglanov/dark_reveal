from django.shortcuts import render


def header(request):
    return render(request, "partials/header.html")

def homepage(request):
    return render(request, "web/homepage.html")

def base(request):
    return render(request, "web/base.html")

def static_section(request):
    return render(request, "web/static_section.html")