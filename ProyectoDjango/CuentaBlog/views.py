from tkinter import image_names
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'CuentaBlog/blog_crear_cuenta.html'
  success_url = reverse_lazy('blogLogin')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class BlogProfile(DetailView):

    model = User
    template_name = "CuentaBlog/user_detail.html"


class BlogUpdate(LoginRequiredMixin, UpdateView):

    model = User
    template_name = "CuentaBlog/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]
    
    
    
    def get_success_url(self):
      return reverse_lazy("blog_profile", kwargs={"pk": self.request.user.id})