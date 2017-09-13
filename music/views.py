from django.shortcuts import render

from music.models import Album
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'music/albumIndex.html', context)


def albumIndex(request):
    album_list = Album.objects.order_by('-num_starts')[:5]
    context = {
        'album_list': album_list,
    }
    return render(request, 'music/albumIndex.html', context)
