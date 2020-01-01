from django.shortcuts import render
from user.forms import LoginForm

# Create your views here.


def login(request):

    login_form = LoginForm()
    return render(request, 'user/login.html', locals())
