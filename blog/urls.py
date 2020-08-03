from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import logout_then_login as auth_logout_login
from .views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    # url(r'^logout/$', LogoutView.as_view(template_name='blog/registration/logged_out.html'), name='logout'),
    url(r'^logout-then-login/$', auth_logout_login, name='logout_then_login'),
    url(r'^user/$', UserView.as_view(), name='user_page_url'),
    url(r'^user/position/new?$', CreateExperience.as_view(), name='experience_create_url'),
    url(r'^user/education/new?$', CreateEducation.as_view(), name='education_create_url'),
    # url(r'^position/update/?$', UpdateExperience.as_view(), name='experience_update_url'),
    url(r'^position/(\d+)/update/?$', UpdateExperience.as_view(), name='experience_update_url'),
]
