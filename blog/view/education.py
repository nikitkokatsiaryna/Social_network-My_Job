import re
from django.views import View
from django.shortcuts import render
from ..form.education import EducationForm
from ..models import Education


class EducationView(View):

    def index(self, request):
        education = Education.objects.filter(user=request.user)
        return render(request, 'blog/experiences/index.html', {'education': education})

    def new(self, request):
        form_education = EducationForm()
        return render(request, 'blog/experiences/new.html', {'form_education': form_education})

    def create(self, request):
        pass

    def show(self, request, id):
        pass

    def edit(self, request, id):
        education_obj = Education.objects.get(id=id)

        context = {
            'object': education_obj,
            'update': True,
            'form': EducationForm(instance=education_obj),
        }

        return render(request, 'blog/experiences/edit.html', context=context)

    def update(self, request, id):
        exp_obj = Education.objects.get(id=id)
        exp_form = EducationForm(request.POST, instance=exp_obj)

        if exp_form.is_valid():
            exp_form.save()

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
        self.create(request, *params)

    def patch(self, request, *params):
        self.update(request, *params)

    def delete(self, request, *params):
        self.destroy(request, *params)
