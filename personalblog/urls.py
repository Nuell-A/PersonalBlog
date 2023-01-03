from django.urls import path
from .views import HomeView, PostDetailView

'''
For the 'name' parameter below, those will be used to 
reference them in HTML templates (for links). 
'''
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # <int:pk> being the primary key of each post (created automatically)
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_details'),
]
