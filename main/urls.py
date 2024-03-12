from django.urls import path
from main.views import RegisterView, LoginView, MainView, AccountView

urlpatterns = [
    path("", MainView.as_view(), name="index"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("account/<int:pk>/", AccountView.as_view(), name="account"),
]

# Step 1
