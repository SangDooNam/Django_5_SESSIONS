from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.http.request import HttpRequest as HttpRequest
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
# Create your views here.


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'common/login.html'
    redirect_authenticated_user =True

    def get_success_url(self) -> str:
        return reverse_lazy('home')
    
    def form_valid(self, form):
        
        
        response = super().form_valid(form)
        
        user_role = self.request.user.role
        
        if user_role in ['admin', 'editor']:
            self.request.session['can_write_notes'] = True
        else:
            self.request.session['can_write_notes'] = False
        
        return response
    
    def dispatch(self, request: HttpRequest, *args: reverse_lazy, **kwargs: reverse_lazy) -> HttpResponse:
        if self.redirect_authenticated_user and request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

def log_out(request):
    logout(request)
    return redirect('home')