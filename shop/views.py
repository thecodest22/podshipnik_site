from django.shortcuts import render


def main(request, **kwargs):
    return render(request, 'shop/index.html')

def about_us(request, **kwargs):
    return render(request, 'shop/about.html')
