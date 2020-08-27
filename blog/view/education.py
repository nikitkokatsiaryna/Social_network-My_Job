import re
from django.views import View
from django.shortcuts import render
from ..form.education import EducationForm
from ..models import Education


class EducationView(View):

    def index(self, request):
        education = Education.objects.filter(user=request.user)
        return render(request, 'blog/education/index.html', {'education': education})

    def new(self, request):
        form_education = EducationForm()
        return render(request, 'blog/education/new.html', {'form_education': form_education})

    def create(self, request):
        template = 'blog/education/index.html'

        bound_form = EducationForm(request.POST)

        if bound_form.is_valid():
            new_exp = bound_form.save(commit=False)
            new_exp.user = request.user
            new_exp.save()

            return render(request, template, {'form': new_exp})

        return render(request, template, {'form': bound_form})

    def show(self, request, id):
        pass

    def edit(self, request, id):
        education_obj = Education.objects.get(id=id)

        context = {
            'object': education_obj,
            'update': True,
            'form': EducationForm(instance=education_obj),
        }

        return render(request, 'blog/education/edit.html', context=context)

    def update(self, request, id):
        educ_obj = Education.objects.get(id=id)
        educ_form = EducationForm(request.POST, instance=educ_obj)

        if educ_form.is_valid():    # form.is_valid = False
            educ_form.save()

    def destroy(self, request, id):
        pass

    def get(self, request, *params):
        if re.match(r'.*new/?$', request.path):
            return self.new(request, *params)
        elif re.match(r'.*edit/?$', request.path):
            return self.edit(request, *params)
        elif re.match(r'.*(\d+)/?$', request.path):
            return self.show(request, *params)
        else:
            return self.index(request, *params)

    def post(self, request, *params):
        return self.create(request, *params)

    def patch(self, request, *params):
        return self.update(request, *params)

    def delete(self, request, *params):
        self.destroy(request, *params)
