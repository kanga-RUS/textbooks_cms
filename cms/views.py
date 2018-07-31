from django.shortcuts import render
from django.views.generic.base import View
from textbooks.models import Textbook

class Custom500View(View):
    def dispatch(self, request, *args, **kwargs):
        return render(request, '404.html')

def error404(request):
    return render(request, '404.html')

def home(request):
    count = Textbook.objects.all().count()
    return render(request, 'home.html', {'count': count})








