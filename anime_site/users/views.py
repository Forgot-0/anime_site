from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import CusetomUserForm, CustomUserCreationsForm
import requests
from .models import CustomUser

# Create your views here.
class RegisterUser(CreateView):
    model = CustomUser
    template_name = 'user/register.html'
    form_class = CustomUserCreationsForm

    def get_success_url(self) -> str:
        return reverse('login')


class LoginUser(LoginView):
    model = CustomUser
    template_name = 'user/login.html'

    def get_success_url(self) -> str:
        return reverse('anime_list')
    
def activation_email(request, uid, token):
    protocol = 'https://' if request.is_secure() else 'http://'
    web_url = protocol + request.get_host()
    post_url = web_url + "/auth/users/activation/"
    post_data = {'uid': uid, 'token': token}
    result = requests.post(post_url, data = post_data)
    content = result.text
    return render(request, '_base.html')