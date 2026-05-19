from django.http import JsonResponse
from django.shortcuts import redirect, render

from myapp.models import Order



# Create your views here.

def index(request):
    return render(request, 'index.html')    
def about(request):
    return render(request, 'aboutus.html')
def chicken(request):
    return render(request, 'chicken.html')
def cows(request):
    return render(request, 'cows.html')
def crop(request):
    return render(request, 'crop.html')
def customer(request):
    return render(request, 'customer.html')
def ducks(request):
    return render(request, 'ducks.html')
def goat(request):
    return render(request, 'goat.html')
def goose(request):
    return render(request, 'goose.html')
def groundnuts(request):
    return render(request, 'groundnuts.html')
def apiculture(request):
    return render(request, 'apiculture.html')
def livestock(request):
    return render(request, 'livestock.html')
def onion(request):
    return render(request, 'onion.html')
def poultry(request):
    return render(request, 'poultry.html')
def sheep(request):
    return render(request, 'sheep.html')
def thankyou(request):
    return render(request, 'thankyou.html')
def watermelon(request):
    return render(request, 'watermelon.html')
from .mpesa import stk_push
from django.views.decorators.csrf import csrf_exempt
import json

def pay(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        amount = request.POST.get('amount')
        result = stk_push(phone, amount)
        return render(request, 'payment_pending.html', {'result': result})
    return render(request, 'pay.html')

@csrf_exempt
def mpesa_callback(request):
    data = json.loads(request.body)
    # Save payment result to database here
    print(data)
    return JsonResponse({'status': 'ok'})
from django.core.mail import send_mail

from django.core.mail import send_mail
from django.shortcuts import redirect

def customer(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        county = request.POST.get('county')
        town = request.POST.get('town')
        delivery = request.POST.get('delivery')
        notes = request.POST.get('notes')
        crops_order = request.POST.get('crops_order')
        order_total = request.POST.get('order_total')
        source = request.POST.get('source')

def customer(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        county = request.POST.get('county')
        town = request.POST.get('town')
        delivery = request.POST.get('delivery')
        notes = request.POST.get('notes')
        crops_order = request.POST.get('crops_order')
        order_total = request.POST.get('order_total')
        source = request.POST.get('source')

        from .models import Order
        Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            county=county,
            town=town,
            delivery=delivery,
            notes=notes,
            crops_order=crops_order,
            order_total=order_total,
            source=source,
        )
        return redirect('thankyou')
    return render(request, 'customer.html')