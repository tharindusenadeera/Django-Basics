from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is the music app homepage</h1>")


def detail(request, album_id):
    return HttpResponse("<h2>This page shows details about music id " + str(album_id) + "</h2>")
