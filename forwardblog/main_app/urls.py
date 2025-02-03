from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.post_index, name='post-index'),
    path('posts/<int:post_id>/', views.post_detail, name="post-detail"),
    path('posts/create/', views.PostCreate.as_view(), name='post-create'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='post-delete'),
    path('books/', views.book_index, name='book-index'),
    path('books/<int:book_id>/', views.book_detail, name="book-detail"),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete', views.BookDelete.as_view(), name='book-delete'),
    
]