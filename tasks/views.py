from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import escape

from tasks.models import Collection, Task


def index(request):
    collection_slug = request.GET.get("collection")

    collection = Collection.get_default_collection()

    if collection_slug:
        collection = get_object_or_404(Collection, pk=collection_slug)

    # All collections
    collections = Collection.objects.order_by("slug")
    tasks = collection.task_set.order_by("description")

    context = {
        'collections': collections,
        'tasks': tasks,
        'collection': collection,
    }
    return render(request, 'tasks/index.html', context)


def add_collection(request):
    collection_name = ''
    if request.method == 'POST':
        # Get collection value from form
        collection_name = escape(request.POST.get("collection_name"))

        # Create new collection
        from django.utils.text import slugify
        collection, created = Collection.objects.get_or_create(name=collection_name, slug=slugify(collection_name))

        if not created:
            # status code 409 for front treatment.
            return HttpResponse("La Collection existe dejà", status=409)

    context = {
        'collection': collection,
    }

    return render(request, 'tasks/collections.html', context)


def add_task(request):
    collection_slug_from_url = int(request.POST.get('collection'))
    task_description = escape(request.POST.get('task_description'))
    collection = Collection.objects.get(slug=collection_slug_from_url)

    task = Task.objects.create(description=task_description, collection=collection)

    context = {
        'task': task,
    }

    return render(request, 'tasks/task.html', context)


def get_tasks(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    tasks = collection.task_set.order_by("description")
    context = {
        'tasks': tasks,
        'collection': collection,
    }
    return render(request, 'tasks/tasks.html', context)


def delete_task(request, task_pk):
    task = get_object_or_404(Task, pk=task_pk)
    task.delete()
    return HttpResponse("")


def delete_collection(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    collection.delete()
    return redirect('home')
