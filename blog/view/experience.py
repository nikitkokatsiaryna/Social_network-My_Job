import re
from django.views import View
from django.shortcuts import render
from ..form.experience import ExperienceForm
from ..models import Experience
from django.shortcuts import redirect


class ExperienceView(View):

    def index(self, request):
        experiences = Experience.objects.filter(user=request.user)
        return render(request, 'blog/experiences/index.html',
                      {'experiences': experiences})

    def new(self, request):
        form_experience = ExperienceForm()
        return render(request, 'blog/experiences/new.html', {'form_experience': form_experience})

    def create(self, request):
        template = 'blog/experiences/index.html'

        bound_form = ExperienceForm(request.POST)

        if bound_form.is_valid():
            new_exp = bound_form.save(commit=False)
            new_exp.user = request.user
            new_exp.save()

            return redirect('/user/')
            # return render(request, template, {'form': new_exp})

        return render(request, template, {'form': bound_form})

    def show(self, request, id):
        pass

    def edit(self, request, id):
        exp_obj = Experience.objects.get(id=id)

        context = {
            'object': exp_obj,
            'update': True,
            'exp_form': ExperienceForm(instance=exp_obj),
        }

        return render(request, 'blog/experiences/edit.html', context=context)

    def update(self, request, id):
        exp_obj = Experience.objects.get(id=id)
        exp_form = ExperienceForm(request.POST, instance=exp_obj)

        if exp_form.is_valid():
            exp_form.save()

        return redirect('/user/')

    def destroy(self, request, id):
        exp_obj = Experience.objects.get(id=id)
        exp_obj.delete()

        context = {
            'object': exp_obj,
        }

        return render(request, 'blog/experiences/index.html',
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
