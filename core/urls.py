from django.urls import path,include
from .views import RegisterApiView,\
                   LoginApiView,\
                   UserAPIView,\
                   RefreshAPIView,\
                   LogoutAPIView

urlpatterns = [
    path("register", RegisterApiView.as_view()),
    path("login", LoginApiView.as_view()),
    path("user", UserAPIView.as_view()),
    path("refresh", RefreshAPIView.as_view()),
    path("logout", LogoutAPIView.as_view()),
]
