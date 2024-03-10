from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView


class MainView(TemplateView):
    template_name = "index.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = "login/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(LoginView):
    template_name = "login.html"
