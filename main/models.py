from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, default=1,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"
