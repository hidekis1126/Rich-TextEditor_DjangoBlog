from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_create, name='post_create'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('blog/image-upload/', views.image_upload, name='image_upload'),
    path('image-upload/', views.image_upload, name='image_upload'),
    path('bulk_delete/', views.post_bulk_delete, name='post_bulk_delete'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),  # Added this line
]
