from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Tag, ToDoList, Item
from .forms import CreateNewList


def home(request):
    user = request.user
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags, "user":user})


def contact(request):
    return render(request, "contact.html")

def todo(request, id=None):
    ls = ToDoList.objects.all()
    if id is not None:
        obj = ToDoList.objects.get(id=id)
        #return HttpResponse("<h1>%s</h1" % id)
        #try:
            #items = ls.item_set.all()
        #except Item.DoesNotExist:
            #items = None  # or handle the case as needed
        #return HttpResponse("<h1>%s</h1>" %(ls.name))
        return render(request, 'todo.html', {"obj": obj, "ls": None})
    else:
        return render(request, 'todo.html', {"ls": ls})

def createitem(request, id=None):
    #ls = ToDoList.objects.get(id=id)
    #return HttpResponse("<h1>%s</h1><br/><p>%i</p>" %(ls.name, id))
    if id is not None :
        ls = ToDoList.objects.get(id=id)
        if request.method == "POST":
            print(request.POST)
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    if request.POST.get('c'+ str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif request.POST.get("newItem"):
                txt = request.POST.get("new")
                if len(txt)> 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")
        return render(request, "createitem.html", {"obj":ls})
    else:
        listAll = ToDoList.objects.all()
        if request.method == "POST":
          if 'goto' in request.POST:
            item_id = request.POST['goto']
            return HttpResponseRedirect("/createitem/%s/" %item_id)
          elif 'delete' in request.POST:
            item_id = request.POST['delete']
            remove = listAll.get(id=item_id)
            remove.delete()
            return HttpResponseRedirect("/createitem/")
        return render(request, "createitem.html", {"obj":None, "ls": listAll})


def createitembootstrap(request, id=None):
    #ls = ToDoList.objects.get(id=id)
    #return HttpResponse("<h1>%s</h1><br/><p>%i</p>" %(ls.name, id))
    if id is not None :
        ls = ToDoList.objects.get(id=id)
        if request.method == "POST":
            print(request.POST)
            if request.POST.get("save"):
                for item in ls.item_set.all():
                    if request.POST.get('c'+ str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif request.POST.get("newItem"):
                txt = request.POST.get("new")
                if len(txt)> 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid")
        return render(request, "createitembootstrap.html", {"obj":ls})
    else:
        listAll = ToDoList.objects.all()
        if request.method == "POST":
          if 'goto' in request.POST:
            item_id = request.POST['goto']
            return HttpResponseRedirect("/createitembootstrap/%s/" %item_id)
          elif 'delete' in request.POST:
            item_id = request.POST['delete']
            remove = listAll.get(id=item_id)
            remove.delete()
            return HttpResponseRedirect("/createitem/")
        return render(request, "createitembootstrap.html", {"obj":None, "ls": listAll})


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            request.user.todolist.add(t)

        return HttpResponseRedirect("/todo/%i" %t.id)

    else:
        form = CreateNewList()
    return render(request, "create.html", {"form": form})


def view(request):
    user = request.user
    ls = request.user.todolist.all()
    print(ls)
    return render(request, 'view.html', {'user': user, 'ls': ls})


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})
