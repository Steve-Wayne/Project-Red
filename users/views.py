from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
# Create your views here.
from.forms import UserCreationForm
def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'users/register.html', {'form':form})    


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html' , {})

