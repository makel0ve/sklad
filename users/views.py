from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def users(request):
    return render(request, 'users/users.html')

class LoginView(TemplateView):
    template_name = "registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("choice/")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


def LogoutView(request):
    logout(request)
    return render(request, 'users/users.html')