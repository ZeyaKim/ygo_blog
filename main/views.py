from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView


class MainView:
    pass


class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = "login/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
