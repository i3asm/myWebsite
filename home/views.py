from django.shortcuts import render
from github import Github
from os import getenv


def index(request):
    g = Github(getenv('GITHUB'))
    context = {
        'repos': g.get_user('i3asm').get_repos()
    }
    return render(request, 'home/index.html', context)
