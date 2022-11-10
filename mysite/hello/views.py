from django.shortcuts import render

# Create your views here.

#Defines a View Function
# This renders an html file
def hello(request):
    return render(request, 'hello.html', {})
