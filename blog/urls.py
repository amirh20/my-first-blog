from django.urls import path
from . import views
app_name='blog'
urlpatterns=[
    path('',views.PostListView.as_view(),name='post_list'),
    path('blog/<int:id>/',views.PostDetailView.as_view(),name='post_detail'),
    path('blog/post/new/',views.PostNewView.as_view(),name='post_new' ),
]