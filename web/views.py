from markdown import Markdown
from django.shortcuts import render
from .models import IndexPicture, Project

def index(request):
    indexAllPictures = IndexPicture.objects.all()
    context = {}
    Last = indexAllPictures.last()
    secondLasts = indexAllPictures.filter(pk=indexAllPictures.last().pk - 1)
    if secondLasts:
        secondLast = secondLasts[0]
    thirdLasts = indexAllPictures.filter(pk=indexAllPictures.last().pk - 1)
    if thirdLasts:
        thirdLast = thirdLasts[0]
    context['Last'] = Last
    context['secondLasts'] = secondLast
    context['thirdLasts'] = thirdLast
    return render(request, 'init/index.html', context)

def services(request):
    allProject = Project.objects.all()
    context = {}
    context['allProject'] = allProject
    return render(request, 'init/services.html', context)


def test1(request):
    return render(request, 'init/test1.html')


def detail(request, id):
    finds = Project.objects.filter(id=id)
    if finds:
        find = finds[0]
    else:
        find = None

    markdowner = Markdown()
    find.content = markdowner.convert(find.content)

    context = {}
    context['find'] = find
    return render(request, 'init/detail.html', context)