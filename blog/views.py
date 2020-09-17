from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.views import View
from .form.experience import ExperienceForm


@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')


class UserView(View):
    def get(self, request):
        form_experience = ExperienceForm()
        experience = Experience.objects.filter(user=request.user)
        education = Education.objects.filter(user=request.user.id)

        context = {'experience': experience,
                   'education': education, 'form_experience': form_experience}

        return render(request, 'blog/user_page.html', context)
