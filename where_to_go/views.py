from django.shortcuts import render


def show_places(request):
    return render(request, 'index.html')