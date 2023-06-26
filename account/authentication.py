from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (CustomUser.DoesNotExist, CustomUser.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None


# def create_profile(backend, user, *args, **kwargs):
#     """
#     Create user profile for social authentication
#     """
#     CustomUser.objects.get_or_create(username=user)
