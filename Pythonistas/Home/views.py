from django.shortcuts import render
from django.views.generic import View,TemplateView,CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from . import forms
# Create your views here.
class temp(View):
    def get(self,request):
        template_name = 'Home/HomePage.html'
        return render(request,template_name)

class Testpage(TemplateView):
    template_name = 'test.html'


class Thankspage(TemplateView):
    template_name = 'thanks.html'


class Index(TemplateView):
    def get(self,request):
        template_name = 'base.html'
        return render(request,template_name)

class Resume(TemplateView):
    def get(self,request):
        template_name = 'resume.html'
        return render(request,template_name)

class HomePage(TemplateView):
    template_name = 'HomePage.html'


class SignUp(CreateView):
    form_class = forms.UserCreateform
    success_url = reverse_lazy('login')
    template_name = 'Home/Signup.html'
