from ..form.registration import RegistrationForm, SignUpForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)

            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.check_password(user_form.cleaned_data['password'])

            # Save the User object
            new_user.save()
            return redirect('blog:sign_up')
    else:
        user_form = RegistrationForm()
    return render(request, 'blog/registration/register.html', {'user_form': user_form})


def sign_up(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)

            User.first_name = new_user.first_name
            new_user.save()
            return redirect('blog:sign_up')
    else:
        user_form = SignUpForm()

    return render(request, 'blog/registration/sign_up.html', {'user_form': user_form})
