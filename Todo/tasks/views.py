from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm



# Create your views here.

def home(request):
    form = TaskForm()
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')


    context = {'tasks':tasks,'taskform':form}

    return render(request,'home.html',context)



def updatetask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        
        return redirect('/')
    
    context = {'taskform':form}

    return render(request,'update.html',context)



def deletetask(request,pk):
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    context = {'task':task}
    return render(request,'delete.html',context)












