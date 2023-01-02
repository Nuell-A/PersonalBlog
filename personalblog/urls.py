from django.urls import path
#from . import views
from .views import HomeView, PostDetailView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),

    # <int:pk> being the primary key of each post (created automatically)
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_details'),
]
