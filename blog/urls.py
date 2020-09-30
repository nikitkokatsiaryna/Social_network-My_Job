from django.conf.urls import url

from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
# from django.contrib.auth.views import logout_then_login
from django.contrib.auth import views as auth_views
from .views import *
from .view.experience import *
from .view.registration import *
from .view.education import *
from .view.certificate import *
from .view.skills import *
from .view.profile import *
from .view.friends import *

# from .view.user_page import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', LoginView.as_view(template_name='blog/registration/login.html'), name='login'),
    url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    # url(r'^register/$', RegistrationView.as_view(), name='register'),
    url(r'^register/$', register, name='register'),
    url(r'^user/$', HomeView.as_view(), name='user_page_url'),  # Заменить на UserView из view.user_page.py

    url(r'^experiences/?$', ExperienceView.as_view(), name='experience_index'),  # index, create
    url(r'^experiences/new/?$', ExperienceView.as_view(), name='experience_new'),  # new
    url(r'^experiences/(\d+)/?$', ExperienceView.as_view(), name='experience_show'),  # show, update, destroy
    url(r'^experiences/(\d+)/edit/?$', ExperienceView.as_view(), name='experience_edit'),  # edit
    # url(r'^experiences/(\d+)/?$', ExperienceView.as_view(), name='experience_update'),  # update, destroy

    url(r'^education/?$', EducationView.as_view(), name='education_index'),  # index, create
    url(r'^education/new/?$', EducationView.as_view(), name='education_new'),  # new
    url(r'^education/(\d+)/?$', EducationView.as_view(), name='education_show'),  # show, update, destroy
    url(r'^education/(\d+)/edit/?$', EducationView.as_view(), name='education_edit'),  # edit

    url(r'^certificate/?$', CertificateView.as_view(), name='certificate_index'),  # index, create
    url(r'^certificate/new/?$', CertificateView.as_view(), name='certificate_new'),  # new
    url(r'^certificate/(\d+)/?$', CertificateView.as_view(), name='certificate_show'),  # show, update, destroy
    url(r'^certificate/(\d+)/edit/?$', CertificateView.as_view(), name='certificate_edit'),  # edit

    url(r'^skill/?$', SkillView.as_view(), name='skill_index'),  # index, create
    url(r'^skill/new/?$', SkillView.as_view(), name='skill_new'),  # new
    url(r'^skill/(\d+)/?$', SkillView.as_view(), name='skill_show'),  # show, update, destroy
    url(r'^skill/(\d+)/edit/?$', SkillView.as_view(), name='skill_edit'),  # edit

    url(r'^profile/?$', ProfileView.as_view(), name='profile_index'),  # index, create
    url(r'^profile/new/?$', ProfileView.as_view(), name='profile_new'),  # new
    url(r'^profile/(\d+)/?$', ProfileView.as_view(), name='profile_show'),  # show, update, destroy
    url(r'^profile/(\d+)/edit/?$', ProfileView.as_view(), name='profile_edit'),  # edit

    url(r'^friend/?$', FriendView.as_view(), name='friends'),
    url(r'^friend/(?P<operation>.+)/(?P<id>\d+)/$', FriendView.change_friends, name='change_friends'),
    url(r'^user/friend/(\d+)/show/?$', FriendView.as_view(), name='show_friend_page'),
]
