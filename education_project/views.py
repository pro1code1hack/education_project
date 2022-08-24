from django.shortcuts import render


def render404(request):
    return render(request, '404.html')
