import os
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from gallery.models import Gallery


class GalleryHome(ListView):
    model = Gallery
    template_name = 'gallery/index.html'
    context_object_name = "images"


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class GalleryDetail(DetailView):
    model = Gallery
    template_name = "gallery/detail.html"
    context_object_name = "image"


    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


    def get_first(self):
        first_object = self.get_queryset().latest('created_on')
        return first_object if first_object else None

    def get_last(self):
        last_object = self.get_queryset().earliest('created_on')
        return last_object if last_object else None

    def get_next(self, current_object_date):
        next_object = self.get_queryset().order_by('-created_on').filter(created_on__lt=current_object_date).first()
        return next_object if next_object else None

    def get_previous(self, current_object_date):
        previous_object = self.get_queryset().order_by('created_on').filter(created_on__gt=current_object_date).first()
        return previous_object if previous_object else None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_object_date = self.object.created_on
        context['next_image'] = self.get_next(current_object_date)
        context['last_image'] = self.get_last()
        context['first_image'] = self.get_first()
        context['previous_image'] = self.get_previous(current_object_date)
        return context


@method_decorator(login_required, name='dispatch')
class GalleryDelete(DeleteView):
    model = Gallery
    template_name = 'website/delete.html'
    success_url = reverse_lazy("gallery:home")
    context_object_name = "image"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Supprimer l'image"
        context['object'] = self.get_object().title
        context['url'] = self.success_url
        context['url_title'] = "Retour vers la galerie"
        return context
    
    def form_valid(self,form):
                
        image = self.get_object()
        
        os.remove(str(image.image.path))
                
        return super().form_valid(form)
    
    

