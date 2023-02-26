from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, FormView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.views import View

from .forms import CustomUserCreationForm, CustomerPhotoForm
from .models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

# class ProfilePage(DetailView):
#     model = CustomUser
#     template_name = "accounts/profile_page.html"

class PhotoGet(DetailView):
    model = CustomUser
    template_name = "accounts/profile_page.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomerPhotoForm()
        return context

class ImagePost(SingleObjectMixin, FormView):
    model = CustomUser
    form_class = CustomerPhotoForm
    template_name = "accounts/profile_page.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.save()
        return super().form_valid(form)
    def get_success_url(self):
        user = self.get_object()
        return reverse("profile", kwargs={"pk": user.pk})
class ProfilePage(View):
    def get(self, request, *args, **kwargs):
        view = PhotoGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ImagePost.as_view()
        return view(request, *args, **kwargs)
