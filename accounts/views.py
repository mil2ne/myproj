from django.contrib.auth.views import LoginView as DjangoLoginView

from accounts.forms import LoginForm


class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = "crispy_form.html"


login = LoginView.as_view()
