from django.db import models
from github import Github
from django.http import HttpResponse
from os import getenv


# Create your models here.

print(getenv('GITHUB'))

class Project(models.Model):
    name = models.TextField()
    description = models.TextField()
    last_updated = models.DateTimeField()

    @classmethod
    def create(cls, name, description):
        project = cls(name=name, description=description)
        # do something with the project
        return project

    @classmethod
    def foo(cls):
        g = Github()
        for repo in g.get_user().get_repos():
            return HttpResponse("<h1> " + repo.name + " </h1>")
