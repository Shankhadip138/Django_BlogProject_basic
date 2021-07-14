from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from posts.models import People,BlogContent,Comments
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
# Create your views here.
def startt(request):
    return render(request,'startt.html')

def index(request):
    people = People.objects.order_by('Name')
    content = {'bloggers':people}
    return render(request,'index.html',content)

def Blogs(request,person_id):
    people = People.objects.get(pk=person_id)
    print(people)
    context={'pep':people}
    return render(request,'Blogs.html',context)

def Comments(request,b_id):
    #people = People.objects.get(pk=person_id)  ,p_id
    blogc=BlogContent.objects.get(pk=b_id)
    context = {'blg':blogc}
    return render(request,'Comments.html',context)
