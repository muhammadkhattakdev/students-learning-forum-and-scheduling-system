from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def homepage(request):
    context = {}

    return render(request, 'schedule_app_pages/home.html', context)



