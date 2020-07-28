from django.urls import path
from django.conf.urls import url

from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import logout_then_login as auth_logout_login
# from .views import get
from .views import UserView, ExperienceView, EducationView

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='blog/registration/logged_out.html'), name='logout'),
    url(r'^logout-then-login/$', auth_logout_login, name='logout_then_login'),
    # url(r'^user/$', views.get, name='user_page'),
    url(r'^user/$', UserView.as_view(), name='user_page'),
    url(r'^user/experience/?$', ExperienceView.as_view(), name='user_experience'),
    url(r'^user/education/?$', EducationView.as_view(), name='user_education'),
    url(r'^user/detail/(\d+)/?$', views.experience_detail, name='experience_detail'),
    url(r'^update_page/(\d+)/?$', views.update_page, name='update_page'),
]
