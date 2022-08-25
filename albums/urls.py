from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums, name='list_albums'),
    path('album_title/<int:pk>', views.album_detail, name='album_detail'),
    path('albums/new', views.create_album, name='create_album'),
]
