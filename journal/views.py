from django.shortcuts import render
from django.http import HttpResponse

# Views
def hello(request):
    #return HttpResponse("Hello World")
    return render(request, 'index.html', {})
