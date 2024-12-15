from django.shortcuts import render, redirect
from. models import Coffee


def home(request):
    coffee=Coffee.objects.all()
    return render(request,'home.html',{'coffee':coffee})


def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')

from .forms import OrderForm

def order_now(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'order_now.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')



   
