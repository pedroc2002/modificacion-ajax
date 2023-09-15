from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import UserUpdateForm

User = get_user_model()

class UserDetail(DetailView):
    model = User
    template_name = 'profile.html'

class UserUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_edit.html'

    def get_success_url(self):
        return reverse('account:profile', kwargs={'pk': self.kwargs['pk']})

class PasswordChange(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('account:password_change_done')

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'profile.html'

class UserDelete(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('account:login')