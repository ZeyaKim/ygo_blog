from django.urls import path
from main.views import RegisterView, LoginView, MainView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]

# Step 1
