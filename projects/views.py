import uuid
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .utils import searchProject , paginatProjects
from .models import project, tag
from .forms import projectForm, ReviewForm
from django.contrib.auth.models import User


def pro(request):
    projects, search_query= searchProject(request)
    custom_range , projects =paginatProjects(request,projects,4)
    
    context={'projects':projects, 'search_query': search_query, 'custom_range': custom_range}
    
    return render(request,"projects/projects.html",context)

    


def projectitem(request,pk):
    projectobj = project.objects.get(id=pk)
    form=ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review=form.save(commit=False)
        review.project = projectobj
        review.owner= request.user.profile
        review.save()

        projectobj.getVoteCount()


        messages.success(request, 'Your Review is Succesfully Submitted')
        return redirect ('projectitem', pk = projectobj.id)
    context={
        'project': projectobj,
        'form': form,
    }
    
     
    return render(request,'projects\single-project.html',context)

@login_required(login_url='login')
def create_project(request):
    profile= request.user.profile
    form= projectForm()
    if request.method == 'POST':
        form=projectForm(request.POST, request.FILES)
        if form.is_valid():
           project= form.save(commit=False)
           project.owner=profile
           project.save()
           return redirect('projects')



    context={'form':form}
    return render(request,'projects\project_form.html',context)
@login_required(login_url='login')
def update_project(request,pk):
    profile= request.user.profile
    projects=profile.project_set.get(id=pk)
    form= projectForm(instance=projects)
    if request.method == 'POST':
        form=projectForm(request.POST,request.FILES, instance=projects)
        if form.is_valid():
            form.save()
            return redirect('projects')



    context={'form':form}
    return render(request,'projects\project_form.html',context) 

@login_required(login_url='login')
def delete_project(request,pk):
    profile= request.user.profile
    projects=profile.project_set.get(id=pk)
    if request.method=='POST':
        projects.delete()
        return redirect('projects')

    context={'object':projects}  
    return render(request, 'delete_template.html',context)     