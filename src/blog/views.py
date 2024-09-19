import os
from django.http import request
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView, CreateView, FormView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from blog.form import CommentForm, AnswerForm
from blog.models import BlogPost, Comment, CommentAnswer
from website import settings


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


class BlogPostDetail(DetailView, FormView):
    model = BlogPost
    template_name = "blog/detail.html"
    context_object_name = "post"
    form_class = CommentForm
    #comment_form = CommentForm
    #answer_form = AnswerForm


    #def post(self):

        #return print(self.request.POST)

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

    def form_valid(self, form):
        #print(form)
        #print(form.cleaned_data)
        #print(self.request.POST)

        if "comment-btn" in self.request.POST:
            form.instance.post = self.get_object()
            comment_data = form.cleaned_data
            comment = Comment(post=form.instance.post, author_comment=comment_data["author_comment"], content_comment=comment_data["content_comment"])
            comment.save()

        if "answer-btn" in self.request.POST:
            answer_data = form.cleaned_data
            answer = CommentAnswer(comment=answer_data["comment"], author_answer=answer_data["author_answer"], content_answer=answer_data["content_answer"])
            answer.save()


        return super().form_valid(form)


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
        #context["answer_form"] = self.answer_form()
        #context["comment_form"] = self.comment_form()
        current_object_date = self.object.created_on
        context['next_post'] = self.get_next(current_object_date)
        context['previous_post'] = self.get_previous(current_object_date)

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
        
        



