from ..form.registration import RegistrationForm, SignUpForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from ..models import Profile


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
            return redirect('blog:login')
    else:
        user_form = RegistrationForm()
    return render(request, 'blog/registration/register.html', {'user_form': user_form})
