from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate
from .models import User


def index(request): 
    if request.method == "POST":
        user = request.POST["username"]
        email = request.POST["email"]
        passw = request.POST["password"]    
        
        User.objects.create(user=user, passw=passw, email=email)
        return redirect("/home")
    return render(request, "index.html")

def home(request):
    
    return render(request, "home.html")