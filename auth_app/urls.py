from django.urls import include, path

from auth_app.views import (
    ChangePasswordView,
    LoginApiView,
    LogoutView,
    ProfileAvatarView,
    ProfileView,
    SignUpApiView,
)

app_name = "auth"

urlpatterns = [
    path("sign-out", LogoutView.as_view(), name="logout"),
    path("sign-in", LoginApiView.as_view(), name="login"),
    path("sign-up", SignUpApiView.as_view(), name="registration"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/avatar", ProfileAvatarView.as_view()),
    path("profile/password", ChangePasswordView.as_view()),
]
