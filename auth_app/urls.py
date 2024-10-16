from django.urls import path, include

from auth_app.views import (
    LoginApiView,
    SignUpApiView,
    LogoutView,
    ProfileView,
    ProfileAvatarView,
    ChangePasswordView,
)


urlpatterns = [
    path("sign-out", LogoutView.as_view()),
    path("sign-in", LoginApiView.as_view()),
    path("sign-up", SignUpApiView.as_view()),

    path("profile", ProfileView.as_view()),
    path("profile/avatar", ProfileAvatarView.as_view()),
    path("profile/password", ChangePasswordView.as_view()),
]
