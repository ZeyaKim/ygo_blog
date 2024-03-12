from django.urls import path
from main.views import RegisterView, LoginView, MainView, AccountView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", MainView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("account/<int:pk>/", AccountView.as_view(), name="account"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

# Step 1
