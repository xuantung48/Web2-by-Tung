from django.shortcuts import render
from django.views import View
# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'homepage/index.html')
class Shop(View):
    def get(self, request):
        return render(request, 'homepage/shop.html')
class About(View):
    def get(self, request):
        return render(request, 'homepage/about.html')

class Single(View):
    def get(self, request):
        return render(request, 'homepage/single.html')

class Login(View):
    def get(self, request):
        return render(request, 'homepage/login.html')

class Register(View):
    def get(self, request):
        return render(request, 'homepage/register.html')

class Coming(View):
    def get(self, request):
        return render(request, 'homepage/coming.html')

class Contact(View):
    def get(self, request):
        return render(request, 'homepage/contact.html')