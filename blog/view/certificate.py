import re
from django.views import View
from django.shortcuts import render
from ..form.certificates import CertificateForm
from ..models import Certificate
from django.shortcuts import redirect


class CertificateView(View):

    def index(self, request):
        certificates = Certificate.objects.filter(user=request.user)
        return render(request, 'blog/certificates/index.html', {'certificates': certificates})

    def new(self, request):
        form_certificate = CertificateForm()
        return render(request, 'blog/certificates/new.html', {'form_certificate': form_certificate})

    def create(self, request):
        template = 'blog/certificate/index.html'

        bound_form = CertificateForm(request.POST)

        if bound_form.is_valid():
            new_exp = bound_form.save(commit=False)
            new_exp.user = request.user
            new_exp.save()

            return redirect('/user/')

        return render(request, template, {'form': bound_form})

    def show(self, request, id):
        pass

    def edit(self, request, id):
        certificate_obj = Certificate.objects.get(id=id)

        context = {
            'object': certificate_obj,
            'update': True,
            'form': CertificateForm(instance=certificate_obj),
        }

        return render(request, 'blog/certificates/edit.html', context=context)

    def update(self, request, id):
        educ_obj = Certificate.objects.get(id=id)
        educ_form = CertificateForm(request.POST, instance=educ_obj)

        if educ_form.is_valid():
            educ_form.save()

        return redirect('/user/')

    def destroy(self, request, id):
        exp_obj = Certificate.objects.get(id=id)
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
