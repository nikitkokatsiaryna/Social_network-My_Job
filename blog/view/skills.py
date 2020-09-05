import re
from django.views import View
from django.shortcuts import render
from ..form.skills import SkillForm

from ..models import Skill
from django.shortcuts import redirect


class SkillView(View):

    def index(self, request):
        form_skills = SkillForm()
        skills = Skill.objects.filter(user=request.user)
        return render(request, 'blog/skills/index.html', {'skills': skills, 'form_skills': form_skills})

    def new(self, request):
        pass

    def create(self, request):

        bound_form = SkillForm(request.POST)

        if bound_form.is_valid():
            new_exp = bound_form.save(commit=False)
            new_exp.user = request.user
            new_exp.save()

            return redirect('/user/')

        return redirect('/user/')

        # return render(request, template, {'form': bound_form})

    def show(self, request, id):
        pass

    def edit(self, request, id):
        # certificate_obj = Certificate.objects.get(id=id)
        #
        # context = {
        #     'object': certificate_obj,
        #     'update': True,
        #     'form': CertificateForm(instance=certificate_obj),
        # }

        # return render(request, 'blog/certificates/edit.html', context=context)
        pass

    def update(self, request, id):
        pass

    def destroy(self, request, id):
        exp_obj = Skill.objects.get(id=id)
        exp_obj.delete()

        context = {
            'object': exp_obj,
        }

        return render(request, 'blog/certificates/index.html',
                      context=context)

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
        if '_method' in request.POST:
            if request.POST['_method'].lower() == 'patch':
                return self.patch(request, *params)
            elif request.POST['_method'].lower() == 'delete':
                return self.delete(request, *params)
        else:
            return self.create(request, *params)

    def patch(self, request, *params):
        return self.update(request, *params)

    def delete(self, request, *params):
        return self.destroy(request, *params)
