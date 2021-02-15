
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.models import User


class MyProfileView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )
