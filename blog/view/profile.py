import re
from django.views import View
from django.shortcuts import render
from ..form.profile import ProfileForm
from ..models import *
from django.shortcuts import redirect


class ProfileView(View):
    def index(self, request, id):
        pass

    def new(self, request):
        pass

    def create(self, request):
        pass

    def show(self, request, id):
        profile = Profile.objects.filter(id=id)

        return render(request, 'blog/profile/index.html', {'profile': profile})

    def edit(self, request, id):
        profile_obj = Profile.objects.get(id=id)

        context = {
            'object': profile_obj,
            'update': True,
            'form': ProfileForm(instance=profile_obj),
        }

        return render(request, 'blog/profile/edit.html', context=context)

    def update(self, request, id):
        profile_obj = Profile.objects.get(id=id)

        profile_form = ProfileForm(request.POST, request.FILES, instance=profile_obj)
        if profile_form.is_valid():
            profile_form.save()

        return redirect('/user/')


    def destroy(self, request, id):
        exp_obj = Profile.objects.get(id=id)
        exp_obj.delete()

        context = {
            'object': exp_obj,
        }

        return render(request, 'blog/profile/index.html',
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
        # if request.FILES:
        #     return self.update_image(request, *params)
        # else:
        return self.update(request, *params)


    def delete(self, request, *params):
        return self.destroy(request, *params)
