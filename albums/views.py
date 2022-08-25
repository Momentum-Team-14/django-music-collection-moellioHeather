from django.shortcuts import render, get_object_or_404
from .models import Album
from .forms import AlbumForm
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('list_albums')
    form = AlbumForm()
    return render(request, 'albums/create_albums.html', {'form': form})


class AuthorCreate(CreateView):
    model = Album
    fields = ['title', 'artist', 'release_date']


class AuthUpdate(UpdateView):
    model = Album
    # Not recommended (potential security issue if more fields added)
    fields = '__all__'


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('album')
