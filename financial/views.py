from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Cost, Thing, Category
# Create your views here.



def create_cost(request, user_id):
    if request.method == "POST":
        price = request.POST["price"]
        thing_id = request.POST["thing"]
        date = request.POST["date"]
        user = User.objects.get(id = user_id)

        thing = Thing.objects.get(id = thing_id)
        cost = Cost.objects.create(price = price,thing=thing,date=date,user=user)

        return redirect('panel',user_id)
    
    else:
        return redirect('panel',user_id)
    



def create_thing(request, user_id):
    if request.method == "POST":
        name = request.POST["name"]
        category_id = request.POST["thing"]
        user = User.objects.get(id = user_id)

        category = Category.objects.get(id = category_id)
        thing = Thing.objects.create(name = name ,category=category,user=user)

        return redirect('panel',user_id)
    
    else:
        return redirect('panel',user_id)
    


def create_category(request, user_id):
    if request.method == "POST":
        name = request.POST["name"]
        user = User.objects.get(id = user_id)

        category = Category.objects.create(name = name ,user=user)

        return redirect('panel',user_id)
    
    else:
        return redirect('panel',user_id)