from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TaskModel
from .form import TaskForm
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class InputFormView(CreateView):
    model = TaskModel
    template_name = 'input_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('showtasks')
    
class ShowTasksListView(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    context_object_name = 'data'

class CompletedListView(ListView):
    model = TaskModel
    template_name = 'completed_tasks.html'
    context_object_name = 'data'

class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'delete.html'
    success_url = reverse_lazy('showtasks')

class TaskUpdateView(UpdateView):
    model = TaskModel
    template_name = 'input_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('showtasks')
    

def CompleteTaskUpdateView(request, pk):
    data = TaskModel.objects.all()
    item = TaskModel.objects.get(id=pk)
    item.is_completed = True
    item.save()
    return render(request, 'completed_tasks.html', {'data':data})
