from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    if request.method != "POST":
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            login(request, new_user)

    context = {'form': form}
    return render(request, 'registration/register.html', context)
