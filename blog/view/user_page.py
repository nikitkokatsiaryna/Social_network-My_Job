from django.views import View
from .experience import ExperienceView


class UserView(View):

    def get(self, request, *params):
        return ExperienceView.index(request)
