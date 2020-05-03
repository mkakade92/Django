from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from accounts import forms
from django.views.generic import CreateView
from django.contrib import messages
# Create your views here.

class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login') #once some has successfully signed taake them to login # its reverse_lazy so it won't happen untill the actual sign up
    template_name='accounts/signup.html'
