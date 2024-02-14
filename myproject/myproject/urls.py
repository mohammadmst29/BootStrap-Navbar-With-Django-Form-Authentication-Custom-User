from django.contrib import admin
from django.urls import path
from .views import (
    homepage,
    signupPage,
    signinPage,
    logoutPage,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('homepage/', homepage, name='homepage'),

    path('signupPage/', signupPage, name='signupPage'),
    path('signinPage/', signinPage, name='signinPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
]
