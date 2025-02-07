from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("view/", views.view, name="view"),
    path("todo/", views.todo, name="todo"),
    path("todo/<int:id>/", views.todo, name="todo"),
    path("create/", views.create, name="create"),
    path("createitem/", views.createitem, name="createitem"),
    path("createitem/<int:id>/", views.createitem, name="createitem"),
    path("createitembootstrap/", views.createitembootstrap, name="createitembootstrap"),
    path("createitembootstrap/<int:id>/", views.createitembootstrap, name="createitembootstrap"),
    path("project/<int:id>/", views.project, name="project"),
]
