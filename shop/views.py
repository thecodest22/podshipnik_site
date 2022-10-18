from django.shortcuts import render


def index(request, **kwargs):
    return render(request, 'shop/index.html')
