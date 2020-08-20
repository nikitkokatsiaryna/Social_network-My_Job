from django.conf.urls import url

from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
# from django.contrib.auth.views import logout_then_login
from django.contrib.auth import views as auth_views
from .views import *
from .view.experience import *
from .view.registration import *
# from .view.user_page import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    # url(r'^register/$', RegistrationView.as_view(), name='register'),
    url(r'^register/$', register, name='register'),
    url(r'^user/$', UserView.as_view(), name='user_page_url'), # Заменить на UserView из view.user_page.py

    url(r'^experiences/?$', ExperienceView.as_view(), name='experience_index'),  # index, create
    url(r'^experiences/new/?$', ExperienceView.as_view(), name='experience_new'),  # new
    url(r'^experiences/(\d+)/?$', ExperienceView.as_view(), name='experience_show'),  # show, update, destroy
    url(r'^experiences/(\d+)/edit/?$', ExperienceView.as_view(), name='experience_edit'),  # edit
    # url(r'^experiences/(\d+)/?$', ExperienceView.as_view(), name='experience_update'),  # update, destroy

]
