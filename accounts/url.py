from django.urls import path
from django.views.generic import TemplateView

from .views import AddCommentView
from django.contrib.auth import views as auth_views #views gaya gahza
from django.contrib import admin
from website import settings
urlpatterns = [
    path('signup/', AddCommentView.as_view(), name= 'signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('setting/change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name= 'change_password'),
    path('setting/change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name= 'password_change_done'),

]