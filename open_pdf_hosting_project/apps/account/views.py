from django.contrib.auth.views import LoginView

from .models import CustomUser, CustomGroups


class UserLoginView(LoginView):
    value = 'some'