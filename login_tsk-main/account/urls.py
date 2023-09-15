from django.urls import path
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from .views import *
app_name = 'account'

urlpatterns = [
    path('signup/', CreateView.as_view(
        template_name='signup.html',
        form_class=CustomUserCreationForm,
        success_url='/account/login',
    ), name='signup'),
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserDetail.as_view(), name='profile'),
		path('user_update/<int:pk>/', UserUpdate.as_view(), name='user_update'),
		path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),
		path('user_delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
]