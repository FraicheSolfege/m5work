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
        print(burgers, fries, drinks, total_cost)
        return render(request, "order_total.html", {"burgers": burgers, "fries": fries, "drinks": drinks, "total_cost": total_cost})
    else:
        return render(request, "order_total.html")
    
def near_hundred(request):
    form = CB1FORM(request.GET)
    print(request.GET)
    if form.is_valid():
        num = form.cleaned_data["num"]
        near_hundred = abs(100 - num) <= 10 or abs(200 - num) <= 10
        return render(request, "cb1.html", {"num": num, "near_hundred": near_hundred})
    else:
        return render(request, "cb1.html")
    
def stringsplosion(request):
    form = CB2FORM(request.GET)
    if form.is_valid():
        print("hey")
        word = form.cleaned_data["word"]
        wordsplosion = ''
        for i in range(len(word)):
            wordsplosion += word[:i+1]
        return render(request, "cb2.html", {"word": word, "wordsplosion":wordsplosion})
    else:
        return render(request, "cb2.html")
    
def catdog(request):
    form = CB3FORM(request.GET)
    if form.is_valid():
        is_catdog = form.cleaned_data["is_catdog"]
        catdog = is_catdog.count('cat') == is_catdog.count('dog')
        return render(request, "cb3.html", {"is_catdog": is_catdog, "catdog": catdog})
    else:
        return render(request, "cb3.html")
    
def lone_sum(request):
    form = CB4FORM(request.GET)
    if form.is_valid():
        int1 = form.cleaned_data["int1"]
        int2 = form.cleaned_data["int2"]
        int3 = form.cleaned_data["int3"]
        if int1 == int2 == int3:
            return render(request, "cb4.html", {"int1": int1, "int2": int2, "int3": int3, "lone_sum": 0})
        if int2 == int3:
            return render(request, "cb4.html", {"int1": int1, "int2": int2, "int3": int3, "lone_sum": int1})
        if int1 == int3:
            return render(request, "cb4.html", {"int1": int1, "int2": int2, "int3": int3, "lone_sum": int2})
        if int1 == int2:
            return render(request, "cb4.html", {"int1": int1, "int2": int2, "int3": int3, "lone_sum": int3})
        return render(request, "cb4.html", {"int1": int1, "int2": int2, "int3": int3, "lone_sum": int1 + int2 + int3})
    else:
        return render(request, "cb4.html")
        

