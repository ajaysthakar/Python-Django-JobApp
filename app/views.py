from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import  loader

from app.models import JobPost

# Create your views here.
Job_Title=[
    "MANAGER","TEAM LEAD","JUNIOR ENGG."
]

Job_Desc=[
    "Managing all the ongoing project & resource allocations","Managing all the task of assigned project by diving it with team-met","Development"
]

def hello(request,name):
    context={}
    context["name"]=name
    context['list_o']=['alpha','beta']
    context['isAuthenticated']=False
    return render(request,'hello.html',context)

def Job_list(request):
    # context={'Titles': Job_Title, 'Desc': Job_Desc }
    jobs= JobPost.objects.all()
    context={'jobs':jobs}
    return render(request,'app/index.html',context)

def job_detail(request,slug_id):
    try:
        #context={'title':Job_Title[id],'Descr':Job_Desc[id]}
        job= JobPost.objects.get(slug=slug_id)
        context={'job':job}
        print(context)
        return render(request,'app/job_detail.html',context)
    except:
        return HttpResponseNotFound("Not found ")