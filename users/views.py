from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.forms import CustomUserForm
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView






class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = CustomUserForm
    
    
    def get_success_url(self):
        return reverse('prog_lang:yaziki_programm')


# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/login/")
#     else:
#         form = CustomUserForm()
    
#     return render(
#         request,
#         'register.html',
#         {
#             "form": form
#         }
#     )




class AuthLoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse('yaziki:yaziki_programm')





# def auth_login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('yaziki:yaziki_programm')
#     else:
#         form = AuthenticationForm()
    
#     return render(
#         request,
#         'login.html',
#         {
#             "form": form
#         }
#     )



class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# def auth_logout_view(request):
#     logout(request)
#     return redirect('/login/')