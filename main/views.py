from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, TemplateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class MainView(TemplateView):
    template_name = "index.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = UserCreationForm
    success_url = "/login/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(LoginView):
    template_name = "login.html"


class AccountView(DetailView):
    model = User
    template_name = "account.html"  # 계정 상세 정보를 표시할 템플릿
    context_object_name = "account"  # 템플릿에서 사용할 컨텍스트 객체의 이름
