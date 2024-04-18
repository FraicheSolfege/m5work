from django.shortcuts import render
from app.forms import *
# Create your views here.
def root(request):
    return render(request, "root.html")

def hey_name(request):
    form = HeyNameForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        howdy = f"hey {name}!"
        return render(request, "hey_name.html", {"name":name, "howdy":howdy})
    else:
        return render(request, "hey_name.html")
    
def how_old(request):
    form = HowOldForm(request.GET)
    if form.is_valid():
        endyear = form.cleaned_data["endyear"]
        birthyear = form.cleaned_data["birthyear"]
        age = endyear - birthyear
        return render(request, "future_age.html", {"endyear": endyear, "birthyear": birthyear, "age": age})
    else:
        return render(request, "future_age.html")
    

def order_total(request):
    form = OrderTotalForm(request.GET)
    if form.is_valid():
        burgers=form.cleaned_data["burgers"]
        fries=form.cleaned_data["fries"]
        drinks=form.cleaned_data["drinks"]
        total_cost = 4.5 * burgers + 1.5 * fries + 1 * drinks
        return render(request, "order_total.html", {"burgers": burgers, "fries": fries, "drinks": drinks, "total_cost": total_cost})
    else:
        return render(request, "order_total.html")