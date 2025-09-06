from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'autenticacao/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index') # Redireciona para a index após o login

def custom_logout(request):
    logout(request)
    return redirect('index')