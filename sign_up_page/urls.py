from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup_page'),
    path('login/',views.login,name='login_page'),
    path('forgot_password/',views.forg_pass,name='forg_pass_page'),
]