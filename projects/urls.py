from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path("", views.ProjectList.as_view(), name="project_index"),
    path("<int:pk>/", views.ProjectDetail.as_view(), name="project_detail"),
]