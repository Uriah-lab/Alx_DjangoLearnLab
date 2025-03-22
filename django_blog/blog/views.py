from django.views.generic import ListView
from .models import Post
from django.shortcuts import render
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Create this template
    context_object_name = 'posts'
def home(request):
    return render(request,'blog/home.html')