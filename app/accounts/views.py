
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.models import User


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
    )

    def get_object(self, queryset=None):
        return self.request.user
