from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import  UserProfile

from .forms import RegistrationForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from textbooks.models import Textbook


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    userproflie = get_object_or_404(UserProfile, user_id=request.user.id)
    count = Textbook.objects.all().filter(author_id = request.user.id).count()
    args = {'user': user, 'userprofile': userproflie, 'count': count}
    return render(request, 'accounts/profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('loginsys:view_profile'))
        else:
            return redirect(reverse('loginsys:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
    return render(request, 'accounts/change_password.html', args)