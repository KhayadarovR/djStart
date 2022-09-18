from django.urls import path, include
from .views import *
from my_site import settings

urlpatterns = [
    #path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    #path('cat/<int:category_id>/', get_category, name='category'),
    path('cat/<int:category_id>/', NewsCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('__debug__/', include('debug_toolbar.urls')),
]
