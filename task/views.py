from tokenize import Comment
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from . models import Task
from .forms import TaskForm, EditTaskForm
from django.db.models import Q


class TaskView(ListView):
    model = Task
    template_name = 'tasks.html'

    # Список начинается с последнего
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Task.objects.all()
        context['task_all'] = queryset.count()
        context['task_true'] = queryset.filter(completed=True).count()
        context['task_false'] = queryset.filter(
            completed=False, comment='').count()
        context['task_difficult'] = queryset.filter(
            completed=False).exclude(comment__exact='').count()
        return context


def category_view(request, category_name):
    category_task = Task.objects.filter(
        category=category_name).order_by('-date_created')
    return render(request, 'category.html', {'category_name': category_name, 'category_task': category_task})


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'index.html'
    # fields = '__all__'
    # fields = ('category', 'department', 'initiator', 'phone_number', 'description',)


class UpdateTaskView(UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'update_task.html'
    #fields = ['performer', 'completed', 'date_completed']


class SearchResultsView(ListView):
    model = Task
    template_name = 'search_results.html'

    def get_queryset(self):
        query = (self.request.GET.get("q")).replace('-', '.')
        object_list = Task.objects.filter(
            Q(initiator__iregex=query) | Q(description__iregex=query) | Q(
                performer__iregex=query) | Q(comment__iregex=query) | Q(department__name__iregex=query) | Q(date_created__iregex=query) | Q(date_completed__iregex=query)
        )
        return object_list.order_by('-date_created')
