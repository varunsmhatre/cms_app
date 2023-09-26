from django.urls import path
from .views import PostCreateView, home

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='cms-create'),
    path('get/', home, name='cms-get'),
    path('search/', PostCreateView.as_view(), name='cms-search'),


]