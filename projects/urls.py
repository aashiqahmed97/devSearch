from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.pro, name='projects'),
    path('projectitem/<uuid:pk>/', views.projectitem, name='projectitem'),
    path('create-project/', views.create_project, name='create-project'),
    path('update-project/<uuid:pk>/', views.update_project, name='update-project'),
    path('delete-project/<uuid:pk>/', views.delete_project, name='delete-project'),
]
