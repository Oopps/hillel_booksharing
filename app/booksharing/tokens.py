from annoying.functions import get_object_or_None
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

from accounts.models import User


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, username, timestamp):
        user = get_object_or_None(User, username=username)
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()
