from django.shortcuts import render


def render404(request):
    return render(request, '404.html')
def main_page(request):
    return render(request, 'main.html')
def homework(request):
    return render(request, 'homework.html')
def homework_single(request):
    return render(request, 'homework_single.html')
def textbooks(request):
    return render(request, 'textbooks.html')
def methodical_work(request):
    return render(request, 'methodical_work.html')
