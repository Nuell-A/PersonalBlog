from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# def home(request):
#   return render(request, 'home.html', {})

'''
class-based views do everything automatically for you. After 
giving it a model and template_name they go get it themselves. 
'''
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'