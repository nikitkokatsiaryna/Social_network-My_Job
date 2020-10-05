from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.views import View
from .form.experience import ExperienceForm


@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')


class HomeView(View):
    def get(self, request, id=None):
        if id is None:
            return render(request, 'blog/user_page.html')
        else:
            user = User.objects.get(id=id)
            return render(request, 'blog/user_page.html', {'user': user})
