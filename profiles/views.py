from django.views.generic import TemplateView, UpdateView, FormView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Profile
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404 

class Profiles(FormView):
    """User Profile View"""

    template_name = "profiles/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('tasks')  

    def get_object(self): 
        """Retrieve the Profile instance or raise Http404."""
        pk = self.kwargs.get('pk') 
        return get_object_or_404(Profile, user_id=pk) 

    def get_form_kwargs(self):
        """Pass the current user's profile instance to the form."""
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object() 
        return kwargs

    def form_valid(self, form):
        """Save the form and redirect."""
        form.save()
        return super().form_valid(form)

   
    def get_success_url(self):
        return super().get_success_url()