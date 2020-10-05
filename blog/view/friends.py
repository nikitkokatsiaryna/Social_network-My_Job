import re
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Profile
from django.contrib.auth.models import User
from ..models import Friend
from django.contrib.auth.decorators import login_required

from django.views import View
from django.shortcuts import render
from ..form.profile import ProfileForm


class FriendView(View):

    def index(self, request):
        # TODO: сделать ассоциацию Profile.friends
        #   в одной табличке хранить связи Friends

        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
        except Friend.DoesNotExist:
            friend = None
            return render(request, 'blog/friends/index.html', {'users': users})

        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        return render(request, 'blog/friends/index.html', {'friends': friends, 'users': users})

    def show(self, request):
        # user = Friend.objects.get(current_user=id)
        # return render(request, user)
        pass

    def get(self, request, *params):
        if re.match(r'.*(\d+)/show/?$', request.path):
            return self.show(request, *params)
        else:
            return self.index(request, *params)

    def change_friends(request, operation, id):
        new_friend = User.objects.get(id=id)
        if operation == 'add':
            Friend.make_friend(request.user, new_friend)
        elif operation == 'remove':
            Friend.lose_friend(request.user, new_friend)
        return redirect('blog:user_page_url')

    # @login_required
    # def add_or_remove_friends(self, request, username, verb):
    #     n_f = get_object_or_404(User, username=username)
    #     owner = request.user.userprofile
    #     new_friend = Profile.objects.get(user=n_f)
    #
    #     if verb == "add":
    #         new_friend.followers.add(owner)
    #         Friend.make_friend(owner, new_friend)
    #     else:
    #         new_friend.followers.remove(owner)
    #         Friend.remove_friend(owner, new_friend)
    #
    #     return redirect(new_friend.get_absolute_url())
