from django.shortcuts import render,redirect
from .models import Todo_list
from .forms import TaskForm
# Create your views here.

# task list
def task_list(request):
    tasks = Todo_list.objects.all()
    done = Todo_list.objects.filter(done=True).count()
    pending = Todo_list.objects.filter(done=False).count()
    context = {'tasks': tasks, 'done':done, 'pending':pending}
    return render(request,'to_do/home.html',context)

# add task
def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    context = {'form' : form}
    return render(request, 'to_do/addtask.html', context)

# edit task
def edit_task(request,pk):
    task = Todo_list.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            task.done = False
            task.save()
            return redirect('home-page')
    context = {'form' : form}
    return render(request, 'to_do/edittask.html', context)

# done task
def done_task(request,pk):
    task = Todo_list.objects.get(id=pk)
    task.done = True
    task.save()
    return redirect('home-page')

# delete task
def delete_task(request,pk):
    task = Todo_list.objects.get(id=pk)
    task.delete()
    return redirect('home-page')