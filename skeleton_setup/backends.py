from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class AutoBackend(ModelBackend):
    """
    Login without username or password for debugging purpose
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        return user_model.objects.first()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
