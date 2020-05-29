from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def login_view(request):
    # return HttpResponse("Hello, world. You're at the Login's login_view")
    return render(request, "login_page.html", {})
