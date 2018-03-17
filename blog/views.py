from django.shortcuts import render


def vuk(request):
    return render(request, 'blog/vuk.html')

