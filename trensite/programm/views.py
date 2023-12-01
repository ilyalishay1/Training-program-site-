from django.shortcuts import render, redirect
from .forms import UserPaymentForm
from .models import UserPayment
from django.http import HttpResponseNotFound


def home(request):
    return render(request, 'programm/home.html')


def advantages(request):
    return render(request, 'programm/advantages.html')


def what_includes(request):
    return render(request, 'programm/what_include.html')


def how_looks(request):
    return render(request, 'programm/how_looks.html')


def reviews(request):
    return render(request, 'programm/reviews.html')


def cost(request):
    return render(request, 'programm/cost.html')


def order(request):
    payment = UserPayment.objects.all()
    form = UserPaymentForm()
    context = {'payment': payment, 'form': form}
    if request.method == "POST":
        form = UserPaymentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, 'programm/order.html', context=context)


def privacy_policy(request):
    return render(request, 'programm/privacypolicy.html')


def offer(request):
    return render(request, 'programm/offer.html')


def page_404(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
