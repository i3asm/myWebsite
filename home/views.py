from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from getenv import env
from github import Github


def index(request):

    g = Github(env('GITHUB'))
    for repo in g.get_user().get_repos():
        return HttpResponse('<h1>hello' + repo + 'world</h1>')
