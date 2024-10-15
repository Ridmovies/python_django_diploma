from django.urls import path, include

from auth_app.views import LoginApiView, SignUpApiView, LogoutView


urlpatterns = [
    path("sign-out", LogoutView.as_view()),
    path("sign-in", LoginApiView.as_view()),
    path("sign-up", SignUpApiView.as_view()),
]
