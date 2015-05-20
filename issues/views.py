from django.shortcuts import render
from django.views.generic import TemplateView
from issues.models import Post

class PostView(TemplateView):
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context