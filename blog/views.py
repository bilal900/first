from django.shortcuts import render
from .models import post,Category
from django.views.generic import ListView,DetailView
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q
# Create your views here.
class PostList(ListView):
      model=post
      paginate_by=2
      def get_queryset(self):
       name=self.request.GET.get('q','')
       object_list=post.objects.filter(
         Q(title__icontains=name)|
         Q(description__icontains=name)    
       )
       return object_list



class PostDetail(DetailView):
    model=post 
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
         context["tags"] = Tag.objects.all()
         context["recent_post"] = post.objects.all()[:3]
         return context




class PostsByCategory(ListView):
      model=post
      def get_queryset(self):
       object_list=post.objects.filter(
            Q(category__name__icontains=self.kwargs['slug'])
       )
       return object_list
  


class PostsByTags(ListView):
      model=post
      def get_queryset(self):
       object_list=post.objects.filter(
            Q(tags__name__icontains=self.kwargs['slug'])
       )
       return object_list

