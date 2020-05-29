from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def display_output_view(request):
    return render(request, "display_output_page.html", {})


def display_all_view(request):
    return render(request, "all.csv", {})
