from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import * 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from forum.models import * 


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
        new_student = Student.objects.create(
            user=user,
        )

        login(request, user)
        return redirect('login')

    return render(request, 'authPages/register.html')


@login_required
def profile_page(request):
    user = request.user
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        date_of_birth = request.POST.get('date_of_birth')
        password = request.POST.get('password')


        if email:
            user.email = email
        if username:
            user.username = username
        if date_of_birth:
            user.date_of_birth = date_of_birth
        if password:
            user.set_password(password)

        user.save()
        messages.success(request, "Your profile has been updated successfully!")
        return redirect('user_profile')

    user_is_moderator = ForumModerator.objects.filter(user=request.user).exists()
    # Fetching user's forum posts
    forum_posts = ForumPost.objects.filter(user=user).order_by('-date_time')

    return render(request, 'authPages/profile.html', {'user': user, 'user_is_moderator' : user_is_moderator,  'forum_posts': forum_posts})





