from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import * 
from django.contrib.auth import authenticate



def login_page(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            print("I'm her")
            return redirect('homepage')
        else:
            context['message'] = 'User not found'
    return render(request, 'authPages/login.html')



def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        birth_date = request.POST.get('birth_date')

        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'authPages/register.html', {
                'error': 'Email is already registered.'
            })

        user = CustomUser.objects.create_user(
            email=email, password=password, username=username, date_of_birth=birth_date
        )
        login(request, user)
        return redirect('login')

    return render(request, 'authPages/register.html')


