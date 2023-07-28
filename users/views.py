from django.shortcuts import render, redirect
from django.contrib.auth import login

# custom imports
from .forms import UserRegistrationForm


def register(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            
            # login registered user
            login(request, user)
            return redirect("links:index")

    context = {'form': form}
    return render(request, 'registration/register.html', context)
