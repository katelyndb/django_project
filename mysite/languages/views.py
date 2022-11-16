from django.shortcuts import render
from languages.models import Language

# Create your views here.


def language_list(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    return render(request, 'language_list.html', context)

def language_detail(request, pk):
    language = Language.objects.get(pk=pk)
    context = {
        'language': language
    }
    return render(request, 'language_detail.html', context)

def index(request):
    return render(request, 'index.html', {})