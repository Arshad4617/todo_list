from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . models import Todo
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    context = {
        "todo_items": todo_items
    }
    return render(request, 'app/index.html', context)

@csrf_exempt
def add_todo(request):
    content = request.POST['content']
    current_date = timezone.now()
    created_obj = Todo.objects.create(added_date=current_date, text=content)

    return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id= todo_id).delete()
    return HttpResponseRedirect('/')