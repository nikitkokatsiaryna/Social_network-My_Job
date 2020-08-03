from django.shortcuts import render


# creation Mixin for CreateExperience, CreateEducation

class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, {'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_exp = bound_form.save()
            return render(request, self.template, {'form': new_exp})

        return render(request, self.template, {'form': bound_form})
