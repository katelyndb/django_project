from django.shortcuts import render


# Create your views here.


def cats(request):
    return render(request, 'cats.html', {})
