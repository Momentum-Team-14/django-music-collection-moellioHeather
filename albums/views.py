from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})


def createAlbum(request):
    form = AlbumForm()
    if request.method == "POST":
        # print(request.POST)
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_albums')

    context = {'form': form}
    return render(request, 'albums/create_album.html', context)


def editAlbum(request, pk):

    album = Album.objects.get(pk=pk)
    form = AlbumForm(instance=album)

    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'albums/create_album.html', context)


def deleteAlbum(request, pk):
    context = {}
    return render(request, 'albums/delete.html', context)
