from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Account, Experience, Education
from django.views import View
from .forms import ExperienceForm, EducationForm
from django.urls import reverse_lazy


@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')


def experience_detail(request, id):
    exp_detail = Experience.objects.get(id=id)
    return render(request, 'blog/experience_detail.html', {'exp_detail': exp_detail})


class UserView(View):

    def get(self, request):
        form_experience = ExperienceForm()
        experience = Experience.objects.all()
        form_education = EducationForm()
        education = Education.objects.all()
        context = {'form_experience': form_experience, 'form_education': form_education, 'experience': experience,
                   'education': education}

        return render(request, 'blog/user_page.html', context)


class ExperienceView(View):

    def post(self, request):
        form_experience = ExperienceForm(request.POST)

        if request.method == 'POST':
            if form_experience.is_valid():
                form_experience.save()
                form_experience = form_experience.cleaned_data
                return render(request, 'blog/experience.html', {"form_experience": form_experience, })

            else:
                raise Exception('dfgdfgdfg')


class EducationView(View):

    def post(self, request):
        form_education = EducationForm(request.POST)

        if form_education.is_valid():
            form_education.save()
            form_education = form_education.cleaned_data
            return render(request, 'blog/education.html', {'form_education': form_education})

        else:
            raise Exception('dfgdfgdfg')


# Запись не обновляется, а создаётся новая
def update_page(request, post_id):
    get_experience = Experience.objects.get(id=post_id)

    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=get_experience),
        if form.is_valid():
            form.save()

    context = {
        'get_experience': get_experience,
        'update': True,
        'form': ExperienceForm(instance=get_experience),
    }

    return render(request, 'blog/update_page.html', context)
