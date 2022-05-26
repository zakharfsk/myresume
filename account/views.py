from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import *
from .models import *


def page_login(request):
    context = {
        'title': 'Увійти'
    }

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context['error'] = 'Невірний логін або пароль'

        return render(
            request,
            'login.html',
            context
        )

def page_register(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                err = form.errors.get_json_data()
                array_errors = ''

                for key, value in err.items():
                    array_errors += value[0]['message'] + '<br>'

                context = {
                    'title': 'Зареєструватися',
                    'form': form,
                    'form_error': array_errors
                }

                return render(
                    request,
                    'register.html',
                    context
                )

        context = {
            'title': 'Зареєструватися',
            'form': form
        }

        return render(
            request,
            'register.html',
            context
        )

def logoutUser(request):
    logout(request)
    return redirect('home')

def profile(request, username):

    if request.method == "POST":
        
        user_form = UserForm(request.POST, request.FILES, instance = request.user)
        
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        else:
            messages.error(request, 'Unable to complete request')
        
        return redirect('users-profile', request.POST['username'])
        
    user_form = UserForm(instance = request.user)
    
    return render(
        request,
        'profile.html',
        context = {'title': f'Вітаємо вас, {request.user.username}', 'user': request.user, 'user_form': user_form}
    )

