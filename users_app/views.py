from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
import os

@login_required
@transaction.atomic
def index(request):
    """ View user profile """

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()    
            messages.success(request, 'Profile details updated.')                 
    else:
        user_form = UserForm(instance = request.user)
        profile_form = ProfileForm(instance = request.user.profile)

    context = { 'user_form': user_form,
                'profile_form': profile_form,
    }

    return render(request, 'social/index.html', context)

def users(request):
    """ View all users list """

    users_list = User.objects.filter(is_active=True).select_related('profile')
    context = {'users_list':users_list}
    return render(request, 'social/users.html', context)