from django.shortcuts import render


def index(request):
       return render(request, 'restaurant_app/index.html')