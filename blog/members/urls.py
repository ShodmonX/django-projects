from django.urls import path

from . import views

urlpatterns = [
    path(route='register/', view=views.UserRegisterView.as_view(), name='register'),
    path(route='login/', view=views.UserLoginView.as_view(), name='login'),
    path(route='profile/', view=views.UserProfileView.as_view(), name='profile'),
    path(route='edit-profile/', view=views.UserEditView.as_view(), name='edit_profile'),
    path(route='update-profile/', view=views.UpdateProfileView.as_view(), name='update_profile'),
    path(route='password/', view=views.ChangePasswordView.as_view(), name='change_password'),
    path(route='password-success/', view=views.SuccessPasswordView.as_view(), name='success_password'),
]