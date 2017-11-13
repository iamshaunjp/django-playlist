from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             #  now log the user in
             user = User.objects.get(username=form.cleaned_data.get('username'))
             login(request, user)
             return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })
