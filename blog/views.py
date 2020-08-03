from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.views import View
from .forms import ExperienceForm, EducationForm
from .utils import ObjectCreateMixin


@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')


class UserView(View):

    def get(self, request):
        form_experience = ExperienceForm()
        experience = Experience.objects.filter(user=self.request.user)
        form_education = EducationForm()
        education = Education.objects.all()
        context = {'form_experience': form_experience, 'form_education': form_education, 'experience': experience,
                   'education': education}

        return render(request, 'blog/user_page.html', context)


class CreateExperience(ObjectCreateMixin, View):
    model_form = ExperienceForm
    template = 'blog/experience/experience_create.html'


# Не заходит в функцию
class UpdateExperience(View):
    # def get(self, request):
    def get(self, request, id):
        # exp_post = Experience.objects.all()
        exp_post = Experience.objects.get(id=id)
        bound_form = ExperienceForm(instance=exp_post)
        return render(request, 'blog/experience/experience_update.html', {'post': exp_post, 'form': bound_form})


class CreateEducation(ObjectCreateMixin, View):
    model_form = EducationForm
    template = 'blog/education/education_create.html'
