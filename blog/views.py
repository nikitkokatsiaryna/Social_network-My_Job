from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.views import View
from .form.experience import ExperienceForm

@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             # Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             # Set the chosen password
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.check_password(user_form.cleaned_data['password'])
#             # Save the User object
#             new_user.save()
#             return redirect('blog:login')
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'blog/registration/register.html', {'user_form': user_form})


class UserView(View):
    def get(self, request):
        form_experience = ExperienceForm()
        experience = Experience.objects.filter(user=request.user)
        # form_education = EducationForm()
        education = Education.objects.filter(user=request.user.id)

        context = {'experience': experience,
                   'education': education, 'form_experience': form_experience}

        return render(request, 'blog/user_page.html', context)


# class CreateExperience(ObjectCreateMixin, View):
#     model_form = ExperienceForm
#     template = 'blog/experience/experience_create.html'


# class CreateEducation(ObjectCreateMixin, View):
#     model_form = EducationForm
#     template = 'blog/education/education_create.html'


# Не заходит в функцию
# class UpdateExperience(View):
#     # def get(self, request):
#
#     def get(self, request, id):
#         # exp_post = Experience.objects.all()
#         get_post = Experience.objects.get(id=id)
#
#         if request.method == 'POST':
#             form = ExperienceForm(request.POST, instance=get_post)
#             if form.is_valid():
#                 form.save()
#
#         context = {
#             'get_post': get_post,
#             'update': True,
#             'form': ExperienceForm(instance=get_post),
#         }
#         return render(request, 'blog/experiences/experience_update.html', context=context)


# class UpdateEducation(View):
#     pass