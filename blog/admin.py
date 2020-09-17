from django.contrib import admin
from .models import Experience, Education, Profile, Certificate, Skill

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Profile)
admin.site.register(Certificate)
admin.site.register(Skill)
