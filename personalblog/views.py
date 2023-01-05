from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

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

class AddPostView(CreateView):
    model = Post
    # Belwo we're specifying where Django can go grab the styling for the form
    form_class = PostForm
    template_name = 'add_post.html'

    # You can specify which model fields to use.
    # Below is an example of how to implement all fields from the model.
    #fields = '__all__'    **SINCE we are using forms.py we do not need to specify fields

    # Below is how to specify specfic fields:
    #field = ('title', 'author', 'content')