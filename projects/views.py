from django.shortcuts import render
from projects.models import Project
from django.views.generic import (View, TemplateView, 
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectList(ListView):
    # projects = Project.objects.all()
    # context = {
    #     'projects': projects
    # }
    # return render(request, 'project_index.html', context)
    context_object_name = 'projects'
    model = Project
    template_name = 'projects/project_index.html'

class ProjectDetail(DetailView):
    # project = Project.objects.get(pk=pk)
    # context = {
    #     'project':project
    # }
    # return render(request, 'project_detail.html', context)
    context_object_name = 'project'
    model = Project
    template_name = 'projects/project_detail.html'