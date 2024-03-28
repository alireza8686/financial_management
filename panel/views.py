from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from financial.models import Thing, Category
# Create your views here.


@login_required
def panel(request, user_id):
    if request.user.id == user_id:
        user = request.user
        
        first_name = user.first_name
        last_name = user.last_name

        things = Thing.objects.all().filter(user_id = user_id)
        categories = Category.objects.all().filter(user_id = user_id)
        return render(request, 'panel/panel.html', {"first_name" : first_name , "last_name" : last_name, "things" : things, "categories" : categories})
    else:
        return redirect('login') 