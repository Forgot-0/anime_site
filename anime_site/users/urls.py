from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from .views import LoginUser, RegisterUser, activation_email


urlpatterns = [
    path('login/', LoginUser.as_view(), name='login1'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout1'),
    re_path('verify/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/', activation_email, name='activation_email')
]
