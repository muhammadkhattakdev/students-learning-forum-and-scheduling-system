from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def forum_home(request):
    context = {}

    return render(request, 'forumPages/home.html', context)



