import os
import random

from django.http import request
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, FormView
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from blog.form import CommentForm, ReplyForm
from blog.models import BlogPost, Comment, Reply
from website import settings

from _utils import antispam


class BlogHome(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "blog/detail.html"
    context_object_name = "post"
    spam_question_reponse = antispam()
    form_class = CommentForm
    second_form_class = ReplyForm
    
       
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(self.request.POST, instance = self.object)
        form2 = self.second_form_class(self.request.POST, instance=self.object)
        
            
        if "submit_comment" in self.request.POST:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        
        if "submit_reply" in self.request.POST:
            if form2.is_valid():
                return self.form_valid(form2)
            else:
                return self.form_invalid(form2)
       
    

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

    def form_valid(self, form):
      
         
        if self.request.POST['sp-mail'] == '' and self.request.POST['sp-question'] == self.spam_question_reponse[1]:
            
            if "submit_comment" in self.request.POST:
                form.instance.post = self.get_object()
                comment_data = form.cleaned_data
                comment = Comment(post=form.instance.post, author_comment=comment_data["author_comment"], content_comment=comment_data["content_comment"])
                comment.save()
                    
                    
            if "submit_reply" in self.request.POST:
                reply_data = form.cleaned_data
                reply = Reply(comment= Comment.objects.get(pk=int(self.request.POST['comment'])), author_answer=reply_data["author_answer"], content_answer=reply_data["content_answer"])
                reply.save()


        return redirect(self.get_success_url())

    def form_invalid(self, form):
        context = self.get_context_data()
        return self.render_to_response(context)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

    def get_next(self, current_object_date):
        next_object = self.get_queryset().order_by('-created_on').filter(created_on__lt=current_object_date).first()
        return next_object if next_object else None


    def get_previous(self, current_object_date):
        previous_object = self.get_queryset().order_by('created_on').filter(created_on__gt=current_object_date).first()
        return previous_object if previous_object else None


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_object_date = self.object.created_on
        context['next_post'] = self.get_next(current_object_date)
        context['previous_post'] = self.get_previous(current_object_date)
        context['spam_question'] = self.spam_question_reponse[0]
        context['form'] = self.form_class()
        context['form2'] = self.second_form_class()

        return context
    
   

@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = BlogPost
    template_name = 'website/delete.html'
    success_url = reverse_lazy("blog:home")
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Supprimer l'article"
        context['object'] = self.get_object().title
        context['url'] = self.success_url
        context['url_title'] = "Retour vers le journal"
        
        return context
    
    
    def form_valid(self,form):
                
        post = self.get_object()
        
        os.remove(str(post.thumbnail.path))
        
        for token in post.content.split():
            if token.startswith('src='):
                filepath = token.split('=')[1].strip('"')
                filepath = filepath.replace('/media', str(settings.MEDIA_ROOT))  # resolve path to MEDIA_ROOT
                os.remove(str(filepath))
                
        return super().form_valid(form)
        
        



