from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Account, Experience


@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html', {'section': 'dashboard'})


def create_user_page(request):
    experience_fields = Experience.objects.all()
    return render(request, 'blog/user_page.html', {'experience_fields': experience_fields})


# def crete_experience(request):
#     return render(request, 'blog/experience.html', {'experience': 'experience'})
